boards = []
board_dict = {}
moves = ['.','O','X']
def checkSym(board):
    b = list(board)
    grid = [b[0:3],b[3:6],b[6:]]
    for i in range(8):
        if i%2 == 1:
            #rotate board
            board_temp = [[0 for _ in range(3)] for _ in range(3)]
            for r0,row in enumerate(grid):
                for c0,col in enumerate(row):
                    board_temp[c0][r0] = col
            
        else:
            #reverse rows
            board_temp = []
            for j,row in enumerate(grid):
                row.reverse()
                board_temp.append(row)
        b = makeString(board_temp)
        b = list(b)
        grid = [b[0:3],b[3:6],b[6:]]
        if makeString(board_temp) in boards:
            #found
            return True
    return False

def makeString(board):
    string = ''
    for r in board:
        for c in r:
            string+=str(c)
    return string

def findSpots(board):
    spots=[]
    for p in range(9):
        if board[p]=='.':
            spots.append(p)
    return(spots)

def win(string):
    if string[0] == string[1] == string[2] != '.' or string[3] == string[4] == string[5] != '.' or string[6] == string[7] == string[8] != '.' \
       or string[0] == string[3] == string[6] != '.' or string[1] == string[4] == string[7] != '.' or string[2] == string[5] == string[8] != '.' \
       or string[0] == string[4] == string[8] != '.' or string[2] == string[4] == string[6] != '.' :
        return True
    else:
        return False
    
for i in range(19683):
    c = i
    string = ''
    for j in range(9):
        string+=str(moves[c%3])
        c//=3
    if string.count('.')>1 and string.count('O')-string.count('X')==0 :
        if not checkSym(string) and not win(string):
            boards.append(string)
            board_dict[string] = findSpots(string)

print(len(boards))
boards.sort()
print(len(board_dict))
for board in boards:
    print(board)

import pickle

pickle.dump( board_dict, open( "boards_out.pkl", "wb" ) )  




