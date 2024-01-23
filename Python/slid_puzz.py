# -*- coding: utf-8 -*-
import random
eloc=4
def createBoard():
    res = []
    for i in range(9):
        res.append(0)
    return res

def setboard(s):
    s[0]=1
    s[1]=2
    s[2]=3
    s[3]=8
    s[4]=0
    s[5]=4
    s[6]=7
    s[7]=6
    s[8]=5

def printBoard(x, goal):
    print('---CURRENT---    -----GOAL----')
    for i in range(0,8,3):
        print("|", end='')
        for y in range(i,i+3):
            z= x[y] if x[y] else ' '
            print(' '+str(z), end = ' |')
        print("    |", end='')
        for y in range(i,i+3):
            z= goal[y] if goal[y] else ' '
            print(' '+str(z), end = ' |')
        
        print()
        print('-------------    -------------')
        
def swap(num):
    global eloc
    num_in= x.index(num)
    if num_in+1==eloc or num_in-1==eloc or num_in+3==eloc or num_in-3==eloc:
        eloc,num_in=num_in,eloc
        x[eloc]=0
        x[num_in]=num
        return 1
    return 0
        
def checkwin(goal):
    if x==goal:
        return 1
    return 0
        

x=createBoard()
setboard(x)
goal=x.copy()
random.shuffle(goal)
print(x)
printBoard(x,goal)

while True:
    try:
        y=int(input('Enter your move: '))
    except:
        print("Enter A Number...")
        continue
    if y not in range(1,10):
        print("Enter Number Between 1-9...")
        continue
    if not swap(y):
        print('Invalid move!!')
        continue
    printBoard(x,goal)
    if checkwin(goal):
        print("YOU WON!!")
        break