import math,copy

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

    countX = 0
    countO = 0
    
    for row in board:
        
        for cell in row:
            
            if cell == X:
                countX += 1
            elif cell == O:
                countO += 1
    if countO == countX:
        return X
    else:
        return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    if terminal(board):
        return None
    
    possibleActions = set()
    
    for i in range(len(board)):
        
        for j in range(len(board[i])):
            
            if board[i][j] == EMPTY:
                possibleActions.add((i, j))
    
    return possibleActions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    x,y = action
    
    if len(board) <= x or len(board[x]) <=y or board[x][y] != EMPTY:
        raise Exception("Invalid action")
    
    newBoard = copy.deepcopy(board)
    newBoard[x][y] = player(board)
    
    return newBoard

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    
    for i in range(3):
        
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
        
    if winner(board) is not None:
        return True

    for row in board: 
        for cell in row:
            if cell == EMPTY:
                return False
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
    # TODO: Know which of the player has a turn, if it is X we should maximize, if it is O we should minimize 
    
    if terminal(board):
        return None
    
    p = player(board)
    
    if p == X:
        action, value = maxValue(board)
    else:  
        action , value = minValue(board)
    
    return action

def maxValue(board):
    
    v = -math.inf
    bestAction = None
    
    if terminal(board):
        return None, utility(board)
     
    for action in actions(board):
        _,value = minValue(result(board, action))    
        if v < value:
            v = value 
            bestAction = action 

           
    return bestAction,v

def minValue(board):
    
    v = math.inf
    bestAction = None
    if terminal(board):
        return None, utility(board)
    
    for action in actions(board):
        
        _,value = maxValue(result(board, action))    
        if v  > value:
            v = value 
            bestAction = action 

    return bestAction,v    