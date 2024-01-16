"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy
import math

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
    Xcount = 0
    Ocount = 0

    for row in board:
        Xcount += row.count(X)
        Ocount += row.count(O)

    if Xcount <= Ocount:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    possible_moves = set()

    for row_index, row in enumerate(board):
        for column_index, item in enumerate(row):
            if item == None:
                possible_moves.add((row_index, column_index))
    
    return possible_moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    player_move = player(board)

    new_board = deepcopy(board)
    i, j = action

    if board[i][j] != None:
        raise Exception
    else:
        new_board[i][j] = player_move

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for player in (X, O):
        # check horizontal
        for row in board:
            if row == [player, player, player]:
                return player

        # check vertical
        for i in range(3):
            column = [board[x][i] for x in range(3)]
            if column == [player, player, player]:
                return player

        # check diagonals
        if [board[i][i] for i in range(3)] == [player, player, player]:
            return player

        elif [board[i][-i-1] for i in range(3)] == [player, player, player]:
            return player
    return None
                               

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # game is won by one of the players
    if winner(board) != None:
        return True

    # moves still possible
    for row in board:
        if EMPTY in row:
            return False

    # no possible moves
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    def max_value(board):
        optimal_move = ()
        if terminal(board):
            return utility(board), optimal_move
        else:
            v = -math.inf
            for action in actions(board):
                min = min_value(result(board, action))[0]
                if min > v:
                    v = min
                    optimal_move = action
            return v, optimal_move


    def min_value(board):
        optimal_move = ()
        if terminal(board):
            return utility(board), optimal_move
        else:
            v = math.inf
            for action in actions(board):
                max = max_value(result(board, action))[0]
                if max < v:
                    v = max
                    optimal_move = action
            return v, optimal_move

    curr_player = player(board)

    if terminal(board):
        return None

    if curr_player == X:
        return max_value(board)[1]

    else:
        return min_value(board)[1]
