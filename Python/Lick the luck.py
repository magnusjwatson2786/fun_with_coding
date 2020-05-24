import random
print('Lets lick the luck!!')
morons=[]
while True:
    print('Enter the names:(leave blank to break)')
    name=input()
    if name == '':
        break
    morons = morons + [name]
print('The names are:')
for name in morons:
    print('  ' + name)
print('Lets start the game!')
print('name the quality of the man and i will tell who he/she is!:')
quality=input()
print(morons[random.randint(0, len(morons) - 1)]+' is '+str(quality))
y=input()
