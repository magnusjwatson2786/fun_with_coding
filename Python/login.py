w=0
y=0
x=0
auth='N'
z='asdfghjkl'
users=['arun','chinmay','amartya','anuj','rohan','ankit','johannes']
print('LOGIN')
while auth=='N':
    print('Enter Correct Username')
    w=input()
    if str(w) in users:
        auth='Y'
print('Correct Username')
print('Enter Password')
y=input()

while y!=z:
    print('Enter Correct Password')
    y=input()

print('Welcome Back!')
print ('Press Enter to Exit')
x=input()

