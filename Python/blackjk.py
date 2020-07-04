# CLASSES

#from random import*
import random

class deck:
    

    def __init__(self):
        self.deck=[[1,2,3,4,5,6,7,8,9,10,11,12,13],['Spades','Clubs','Hearts','Diamonds']]
        self.names={1:'Ace', 2:'Two', 3:'Three', 4:'Four', 5:'Five', 6:'Six', 7:'Seven', 8:'Eight', 9:'Nine', 10:'Ten', 11:'Jack', 12:'Queen', 13:'King'}
    def randomgroup(self):
        return self.deck[1][random.randint(0,3)]

    def randomface(self):
        return self.deck[0][random.randint(0,12)]



#                                       Inheritance to be used ////////////////////////////////////// 

class player:

    def __init__(self,funds=100):
        self.myfunds = funds
        self.cards=[]
        self.bet=0
        self.val=0
        self.busts=False
        self.aces=0
    

    def __str__(self):
        return 'Player'

    def blackjack(self):
        print('Fantastic! You won through BlackJack! :-)')
        self.bet=self.bet+self.bet*1.5
        self.myfunds+=self.bet
        self.bet=0
        self.val=0
        self.aces=0
        self.cards.clear()

    def win(self):
        print('You won the game.Cool!')
        self.bet*=2
        self.myfunds+=self.bet
        self.bet=0
        self.val=0
        self.aces=0
        self.cards.clear()

    def bust(self):
        print('You are busted.')
        self.bet=0
        self.val=0
        self.aces=0
        self.cards.clear()
        self.busts=True
    
    def lose(self):
        self.bet=0
        self.val=0
        self.aces=0
        self.cards.clear()
        self.busts=False



class dealer:

    def __init__(self):
        self.cards=[]
        self.val=0
        self.hiddencard=''
        self.busts=False
        self.aces=0

    def hidecard(self):
        if len(self.cards)!=0:
            self.hiddencard=self.cards[1]
            self.cards[1]='Card Faced down'
        else:
            print('No card to hide')

    def revealcard(self):
        if len(self.cards)!=0:
            self.cards[1]=self.hiddencard
            self.hiddencard=''
        else:
            print('No card to reveal')

    def __str__(self):
        return 'Dealer'

    def win(self):
        print('Dealer won the game.Better luck next time!:-(')
        self.val=0
        self.aces=0
        self.cards.clear()

    def bust(self):
        print('Dealer is busted.')
        self.val=0
        self.aces=0
        self.busts=True
        self.cards.clear()

    def lose(self):
        self.val=0
        self.aces=0
        self.cards.clear()
        self.busts=False

#  GAMEPLAY

#Variables
deck1=deck()
player1=player()
dealer1=dealer()
gc=False

#Definitions    
def new_card(group,face,pcards,p):  #                debugged(1found)
    pcards.append(f"{deck1.names[face]} of {group}")
    if face==1:
        p.aces+=1
    p.val+=val_count(face)
    while p.val>21 and p.aces:
        p.val-=10
        p.aces-=1
    

def val_count(f_card):      #                    debugged(ace left)
    if f_card== 1:#---                        ------------>ACE
        return 11
    if f_card in range(2,11) :
        return f_card
    if f_card in range(11,14):
        return 10

def printcards(a):      #                             debugged
    if len(a.cards)!=0:
        print(f"{str(a)} has following cards:")
        for _ in a.cards:
            print(_)
            
        print(a.val)
    else:
        print(f"{str(a)} has no cards.")

def askforbet(b):       #                             debugged
    a=input('Enter your bet amount:')
    try: 
        a=int(a)
    except:
        print('Invalid Input')
        askforbet(b)
    else:
        if a>b.myfunds:
            print(f'Insufficient funds. Your chips:{b.myfunds}')
            askforbet(b)
        else:
            b.myfunds-=a
            b.bet=a

def askforhit():    #                           debugged(multiple bugs found , gameplay adjusted)
    global gc
    while True:
        print("=======================================")
        a=input('Choose HIT or STAY: ').lower()
        print("=======================================")
        if a=='stay':
            print('PLayer stays!')
            break
        elif a=='hit':
            hit(player1)
            if player1.val>21:
                player1.bust()
                gc=True
                break
            if player1.val==21:
                player1.win()
                gc=True
                break
        else:
            print('Not a valid input.')
            askforhit()

def hit(x):         #                             created for gameplay adjustment
    print(f"{str(x)} hits!")
    new_card(deck1.randomgroup(),deck1.randomface(),x.cards,x)
    print("=======================================")
    printcards(x)

def tie():    #                                                debugged
    print('\n')
    print("=======================================")
    print('The Game is Tied :-|')
    print("=======================================")
    player1.myfunds+=player1.bet
    player1.bet=0
    player1.val=0
    player1.cards.clear()
    dealer1.val=0
    dealer1.cards.clear()

def playagain():    #                                       debugged
    a=input('Play Again?(Yes/No):').lower()
    if a=='yes':
        play()
    elif a=='no':
        print('OK then. GoodBye')
        print('\n')
        print("=======================================")
    else:
        print('Not a valid input.')
        playagain()

def gameover():         #                                  debugged
    global gc
    if dealer1.busts:
        player1.win()
    elif player1.busts:
        dealer1.win()
    else:
        print('Good Game!')
    
    gc=False

def play():
    global gc
    print('\n')
    print("=======================================")
    print('Welcome to BlackJack')
    print("=======================================")
    print('\n')
    print("=======================================")
    askforbet(player1)
    print('Your bet has been placed.')
    print("=======================================")
    print('\n')
    new_card(deck1.randomgroup(),deck1.randomface(),player1.cards,player1)
    new_card(deck1.randomgroup(),deck1.randomface(),player1.cards,player1)
    new_card(deck1.randomgroup(),deck1.randomface(),dealer1.cards,dealer1)
    new_card(deck1.randomgroup(),deck1.randomface(),dealer1.cards,dealer1)
    dealer1.hidecard()
    print('\n')
    print("=======================================")
    printcards(dealer1)
    printcards(player1)
    print("=======================================")
    print('\n')

    if player1.val == 21:
            player1.blackjack()
            gc=True

    askforhit()



    if not gc:
        print('\n')
        print("=======================================")
        dealer1.revealcard()
        print('Dealer\'s card is revealed')
        printcards(dealer1)
        print("=======================================")
        print('\n')


        while dealer1.val<17 :
            y=input('Press ENTER to continue.')
            print('\n')
            print("=======================================")
            hit(dealer1)
            if dealer1.val>21:
                dealer1.bust()
                gc=True
                break

            if dealer1.val==21:
                dealer1.win()
                gc=True
                break
    
    

    if not gc:
        y=input('Press ENTER to continue.')
        if dealer1.val==player1.val:
            tie()
        elif dealer1.val>player1.val:
            print("=======================================")
            print('Dealer has a higher hand.')
            print("=======================================")
            dealer1.win()
            player1.lose()
            print("=======================================")
        else:
            print("=======================================")
            print('You have a higher hand.')
            print("=======================================")
            player1.win()
            dealer1.lose()
            print("=======================================")

play()
gameover()
playagain()