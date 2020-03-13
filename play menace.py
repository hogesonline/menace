import random
import pickle

def count_dots(grid):
    count=0
    for i in grid:
        if i=='.':
            count+=1
    return count

def get_rand_move(board):
    poss=[]
    #print(board)
    for n,square in enumerate(board):
        if square=='.':
            poss.append(n+1)
        
    return random.choice(poss)


def found(board,p):
    #board and poss_moves dictionary
    keymove=False
    reverse=True
    counter=0
    temp=0
    timesf=0
    timesr=0
    key=[]
    if ''.join(board) in p:
        keymove=True
        key=board
        return (True,key,timesr+ timesf)
    #check all 8 symmetries and see if it's in the dictionary
    while keymove == False and counter<=8:
        if reverse==True:
            timesr+=1
            for i in range(0,9,3):
                temp=board[i]
                board[i]=board[i+2]
                board[i+2]=temp
            if ''.join(board) in p:
                keymove=True
                key=board
                print(key)
                return (True,key,timesr+timesf)
            reverse=False
        else:
            timesf+=1
            temp=board[1]
            board[1]=board[3]
            board[3]=temp
            temp=board[5]
            board[5]=board[7]
            board[7]=temp
            temp=board[2]
            board[2]=board[6]
            board[6]=temp
            if ''.join(board) in p:
                keymove=True
                key=board
                print(key)
                return (True,key,timesr+timesf)
            reverse=True
    #didn't find it  
    return (False,None,timesr+timesf)

def matchboxmoves(board,p):
    global beads
    
    index="".join(board)
    fnd, board, t = found(board,p)
    poss=p[''.join(board)]
    print(poss)
    if fnd and len(poss)>0:
        moves=poss
        #print(moves)
        m= random.choice(moves)
    else:
        print("No valid moves, computer quits")
        return (False,False)
    beads["".join(board)]=m
    return (m,t)


N = "Computer"
C = "Random"

graphing={}
frstmove=''
count=0
numgames=0
poss_moves=pickle.load(open("matchbox.pkl","rb"))
#print(poss_moves)
qut=False
beads={}
winner=""
win=False
turns=1
grid=['.','.','.','.','.','.','.','.','.']

matchstats={}
print("NOUGHTS AND CROSSES")
print("The computer wil be noughts.")
totgames = 10
print("OK computer goes first!")
move,t = matchboxmoves(grid,poss_moves)
grid[move-1]="O"
temp=grid
count=0
print("-------------")
for i in range( 3):
    a = str(count+1) if grid[count]=='.' else grid[count]
    b = str(count+2) if grid[count+1]=='.' else grid[count+1]
    c = str(count+3) if grid[count+2]=='.' else grid[count+2]
    print("| "+a+" | "+b+" | "+c+" |")
    print("-------------")
    count+=3
loss=False
players=[N,C]
moves = ["O","X"]
while totgames>numgames:
    while win != True and loss!=True and turns<=9:
        if (grid[0]==grid[1]==grid[2] and grid[0] != '.')\
        or (grid[3]==grid[4]==grid[5] and grid[3] != '.')\
        or (grid[6]==grid[7]==grid[8] and grid[6] != '.')\
        or (grid[0]==grid[3]==grid[6] and grid[0] != '.')\
        or (grid[1]==grid[4]==grid[7] and grid[1] != '.')\
        or (grid[2]==grid[5]==grid[8] and grid[2] != '.')\
        or (grid[0]==grid[4]==grid[8] and grid[0] != '.')\
        or (grid[2]==grid[4]==grid[6]and grid[2] != '.'):
           winner=players[(turns+1)%2]
           win=True
           print('win')
           
        else:
            #noughts turn
            print('not win')
            if players[turns%2]== N:
                print('noughts')
                #if it's the last move
                if turns==8:
                    for sq in range(len(grid)):
                        if grid[sq] == '.':
                            grid[sq]="O"
                            turns+=1
                            break
                    count=0
                    print("-------------")
                    for i in range( 3):
                        a = str(count+1) if grid[count]=='.' else grid[count]
                        b = str(count+2) if grid[count+1]=='.' else grid[count+1]
                        c = str(count+3) if grid[count+2]=='.' else grid[count+2]
                        print("| "+a+" | "+b+" | "+c+" |")
                        print("-------------")
                        count+=3
                else:
                    #Any other move
                    move,t=matchboxmoves(grid,poss_moves)
                    if move==False and t==False:
                        loss==True
                    else:
                        grid[move] = "O"
                        turns+=1
                        

            else:
                turns+=1
                print("crosses")
                print("-------------")
                count=0
                for i in range( 3):
                    a = str(count+1) if grid[count]=='.' else grid[count]
                    b = str(count+2) if grid[count+1]=='.' else grid[count+1]
                    c = str(count+3) if grid[count+2]=='.' else grid[count+2]
                    print("| "+a+" | "+b+" | "+c+" |")
                    print("-------------")
                    count+=3
                square = int(input("Human's turn - which square: "))
                square-=1
                grid[square] = "X"
                
    #reset everything
    winner=""
    win=False
    turns=1
    grid=['.','.','.','.','.','.','.','.','.']

    numgames += 1
    
    print("NOUGHTS AND CROSSES")
    print("The computer wil be noughts.")
    print("OK computer goes first!")
    move,t = matchboxmoves(grid,poss_moves)
    grid[move-1]="O"
    temp=grid
    count=0
    print("-------------")
    for i in range( 3):
        a = str(count+1) if grid[count]=='.' else grid[count]
        b = str(count+2) if grid[count+1]=='.' else grid[count+1]
        c = str(count+3) if grid[count+2]=='.' else grid[count+2]
        print("| "+a+" | "+b+" | "+c+" |")
        print("-------------")
        count+=3
    loss=False


for key in boards:
    print (key, boards[key])











            
