def dispboard (board):#function to create a model of tic-tac-toe structure
    print(board[1]+'|'+board[2]+'|'+board[3])
    print('-+-+-')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-+-+-')
    print(board[7]+'|'+board[8]+'|'+board[9])
def blkspc (board,loc):#function to prevent lack of space between separations
    if board[loc]=='':
        board[loc]=' '
        
tttboard={1:' ',2:' ',3:' ',#values of nine places
	  4:' ',5:' ',6:' ',
          7:' ',8:' ',9:' '}
for i in range(1,10):
    blkspc(tttboard,i)
a=0
filled=[]#list to store filled locations
while a<=8 :#loop to continue 9 times to get values for all places
    dispboard(tttboard)#displays the board
    print('Turn for O:')
    print('Enter the location to insert O:')
    markloc=input()
    if markloc=='':
        break
    if int(markloc)>9 or int(markloc)==0:#to prevent invalid value
        print('Invalid Value.Restart the game!')
        break
    if int(markloc) in filled:#to check if the location is already filled
        print('Location already filled.Restart the game!')
        break
    filled.append(int(markloc))
    tttboard[int(markloc)]='O'
    a+=1
    if a==9:#to break when looped 9 times
        print('>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<')
        break
    dispboard(tttboard)
    print('Now the Turn for X:')
    print('Enter the location to insert X:')
    markloc=input()
    if markloc=='':
        break
    if int(markloc)>9 or int(markloc)==0:#same as above
        print('Invalid Value.Restart the game!')
        break
    if int(markloc) in filled:
        print('Location already filled.Restart the game!')#same as above
        break
    filled.append(int(markloc))
    tttboard[int(markloc)]='X'
    a+=1
d=input()   
    
