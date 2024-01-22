def createBoard():
    res = []
    for i in range(3):
        temp = [0] * 3
        res.append(temp)
    return res

def checkWin(board):
    if board[0] == [1,1,1] or board[1] == [1,1,1] or board[2] == [1,1,1]:
        return 1
    if board[0] == [2,2,2] or board[1] == [2,2,2] or board[2] == [2,2,2]:
        return 2
    # boardnp = numpy.array(board) # converting to numpy array
    # board = boardnp.T.tolist() # transposing and converting back to list
    board=list(map(list, zip(*board))) # transposing using zip and map
    if board[0] == [1,1,1] or board[1] == [1,1,1] or board[2] == [1,1,1]:
        return 1
    if board[0] == [2,2,2] or board[1] == [2,2,2] or board[2] == [2,2,2]:
        return 2
    if board[0][0] ==  board[1][1] ==  board[2][2]:
        if board[0][0]==1:
            return 1
        if board[0][0]==2:
            return 2
    if board[0][2] ==  board[1][1] ==  board[2][0]:
        if board[0][2]==1:
            return 1
        if board[0][2]==2:
            return 2
    return 0

def Update(userinp, sym):
    my_dic = {1:(0,0),
              2:(0,1),
              3:(0,2),
              4:(1,0),
              5:(1,1),
              6:(1,2),
              7:(2,0),
              8:(2,1),
              9:(2,2)}
    a,b=my_dic[userinp]
    x[a][b] = sym


def printBoard(x):
    dic={0:" ",1:p1sym,2:p2sym}
    print('---------------')
    for i in x:
        for y in i:
            print("| "+str(dic[y]), end = ' |')
        print()
        print('---------------')
def helper(board):
    print('---------------')
    for i in board:
        for y in i:
            print("| "+str(y), end = ' |')
        print()
        print('---------------')
    

def valid(board, num):
    my_dic = {1:(0,0),
              2:(0,1),
              3:(0,2),
              4:(1,0),
              5:(1,1),
              6:(1,2),
              7:(2,0),
              8:(2,1),
              9:(2,2)}
    x = my_dic[num]
    if board[x[0]][x[1]] == 0:
        return True
    return False

def isfull(board):
    for i in board:
        for j in i:
            if j == 0:
                return False
    return True

def helperBoard(board):
    counter = 1
    for i in range(3):
        for j in range(3):
            board[i][j] = counter
            counter += 1
    return board
            
        
x = createBoard()
y = createBoard()
y = helperBoard(y)
print("Welcome to our tic tac toe game!!".center(60, "*"))
helper(y)

while True:
    p1sym=input('Player1 pick a symbol!(O/X) ').upper()
    if p1sym not in ['O','X']:
        print('Invalid Symbol')
        continue
    p2sym='X' if p1sym=='O' else 'O'
    turn=0
    while True:
        if turn%2==0:
            try:
                p1pos=int(input('Player1 your turn (1~9):'))
            except:
                print("Enter A Number...")
            if p1pos not in range(1,10):
                print("Enter Number Between 1-9...")
                continue
            if valid(x, p1pos):
                Update(p1pos,1)
            else:
                print("Enter Empty Square...")
                continue
        else:
            try:
                p2pos=int(input('Player2 your turn (1~9):'))
            except:
                print("Enter A Number...")
                continue
            if p2pos not in range(1,10):
                print("Enter Number Between 1-9...")
                continue
            if valid(x, p2pos):
                Update(p2pos,2)
            else:
                print("Enter Empty Square...")
                continue
        printBoard(x)
        winner= checkWin(x)
        if winner != 0:
            break
        turn+=1
        if isfull(x):
            break
            
    if winner != 0:
        print(f'Player{winner} won!!')
    else:
        print("It's a Tie!!")
    
    break