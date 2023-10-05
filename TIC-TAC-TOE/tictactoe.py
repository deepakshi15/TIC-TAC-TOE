"""
Tic Tac Toe Player
"""

import math
import copy

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
    Xnumber=0
    Onumber=0

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]==X:
                Xnumber+=1

            if board[i][j]==O:
                Onumber+=1

    if Xnumber > Onumber:
        return O

    else:
        return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    waysofactions=set()

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]==EMPTY:
                waysofactions.add((i,j))
    
    return waysofactions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Invalid Action")
    
    i,j = action
    duplicate_board=copy.deepcopy(board)
    duplicate_board[i][j]=player(board)
    return duplicate_board

def explore_row(board,player):
    for i in range(len(board)):
        if board[i][0]==player and board[i][1]==player and board[i][2]==player:
            return True
    return False

def explore_col(board,player):
    for j in range(len(board)):
        if board[0][j]==player and board[1][j]==player and board[2][j]==player:
            return True
    return False

def firstmove(board,player):
    cnt=0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if i==j and board[i][j]==player:
                cnt+=1
    if cnt==3:
        return True
    else:
        return False

def secondmove(board,player):
    cnt=0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if (len(board)-i-1)==j and board[i][j]==player:
                cnt+=1
    if cnt==3:
        return True
    else:
        return False  

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if explore_row(board,X) or explore_col(board,X) or firstmove(board,X) or secondmove(board,X):
        return X
    elif explore_row(board,O) or explore_col(board,O) or firstmove(board,O) or secondmove(board,O):
        return O
    else:
        return None
    
def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board)==X:
        return True
    if winner(board)==O:
        return True
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]==EMPTY:
                return False
    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board)==X:
        return 1
    elif winner(board)==O:
        return -1
    else:
        return 0

def fun_max_value(board):
    v= -math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v=max(v,fun_min_value(result(board,action)))
    return v

def fun_min_value(board):
    v= math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v=min(v,fun_max_value(result(board,action)))
    return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    # player is X(max player)
    elif player(board)==X:
        moves=[]

        #loop over the possible actions
        for action in actions(board):
            moves.append([fun_min_value(result(board,action)),action])
        return sorted(moves,key=lambda x:x[0],reverse=True)[0][1]
    
    # player is O(min player)
    elif player(board)==O:
        moves=[]

        #loop over the possible actions
        for action in actions(board):
            moves.append([fun_max_value(result(board,action)),action])
        return sorted(moves,key=lambda x:x[0])[0][1]

    

