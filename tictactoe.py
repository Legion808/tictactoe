"""
Tic Tac Toe Player
"""

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # Count the number of X's and O's
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    # If X's count is equal or less than O's, it's X's turn; otherwise, it's O's
    return X if x_count == o_count else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    return {(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY}


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board[action[0]][action[1]] is not EMPTY:
        raise ValueError("Invalid action: Cell is already occupied.")

    new_board = [row[:] for row in board]  # Make a deep copy
    new_board[action[0]][action[1]] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows, columns, and diagonals for a winner
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return winner(board) is not None or all(cell != EMPTY for row in board for cell in row)


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    current_player = player(board)

    if current_player == X:
        _, action = max_value(board)
    else:
        _, action = min_value(board)

    return action


def max_value(board):
    if terminal(board):
        return utility(board), None

    v = float('-inf')
    best_action = None
    for action in actions(board):
        min_result, _ = min_value(result(board, action))
        if min_result > v:
            v = min_result
            best_action = action
        if v == 1:
            break  # Pruning: since we found the best outcome
    return v, best_action


def min_value(board):
    if terminal(board):
        return utility(board), None

    v = float('inf')
    best_action = None
    for action in actions(board):
        max_result, _ = max_value(result(board, action))
        if max_result < v:
            v = max_result
            best_action = action
        if v == -1:
            break  # Pruning: since we found the best outcome
    return v, best_action
