def digit(colvar):
    global digit_conf
    digit_conf=0
    while (digit_conf!=1):
        if colvar=='black':
            digit_conf=1
            return 0
        elif colvar=='brown':
            digit_conf=1
            return 1
        elif colvar=='red':
            digit_conf=1
            return 2
        elif colvar=='orange':
            digit_conf=1
            return 3
        elif colvar=='yellow':
            digit_conf=1
            return 4
        elif colvar=='green':
            digit_conf=1
            return 5
        elif colvar=='blue':
            digit_conf=1
            return 6
        elif colvar=='violet':
            digit_conf=1
            return 7
        elif colvar=='grey':
            digit_conf=1
            return 8
        elif colvar=='white':
            digit_conf=1
            return 9
        else:
            return 'Undesired Value.Retry!'
        
    
def mltplr(colvar):
    global mltplr_conf
    mltplr_conf=0
    while (mltplr_conf!=1):
        if colvar=='black':
            mltplr_conf=1
            return 1
        elif colvar=='brown':
            mltplr_conf=1
            return 10**1
        elif colvar=='red':
            mltplr_conf=1
            return 10**2
        elif colvar=='orange':
            mltplr_conf=1
            return 10**3
        elif colvar=='yellow':
            mltplr_conf=1
            return 10**4
        elif colvar=='green':
            mltplr_conf=1
            return 10**5
        elif colvar=='blue':
            mltplr_conf=1
            return 10**6
        elif colvar=='violet':
            mltplr_conf=1
            return 10**7
        elif colvar=='grey':
            mltplr_conf=1
            return 10**8
        elif colvar=='white':
            mltplr_conf=1
            return 10**9
        else:
            return 'Undesired Value.Retry!'
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>CYBORG ULTRA<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
print('<<<<<<<<<<<<<<<<<<<<<Welcome to Resistor Value Assistant>>>>>>>>>>>>>>>>>>>>')
digit_no_conf=0
while (digit_no_conf!=1):
    print ('Enter no. of digits')
    x=input()

    if (int(x)==1):
        print('Enter the color of 1st strip:')
        a=input()
        p=digit(a)
        print(str(p))
        if digit_conf:
            mltpt=int(p)
            digit_no_conf=1
    
    if (int(x)==2):
        print('Enter the color of 1st strip:')
        a=input()
        p=digit(a)
        print(str(p))
        if digit_conf:
            print('Enter the color of 2nd strip:')
            b=input()
            q=digit(b)
            print(str(q))
            if digit_conf:
                mltpt=int(p*10+q)
                digit_no_conf=1
   
    if (int(x)==3):
        print('Enter the color of 1st strip:')
        a=input()
        p=digit(a)
        print(str(p))
        if digit_conf:
            print('Enter the color of 2nd strip:')
            b=input()
            q=digit(b)
            print(str(q))
            if digit_conf:
                print('Enter the color of 3rd strip:')
                c=input()
                r=digit(c)
                print(str(r))
                if digit_conf:
                    mltpt=int(p*100+q*10+r)
                    digit_no_conf=1
    
    if (int(x)>3):
        print('You are supposed to enter value from 1 to 3!')
    if (int(x)<1):
        print('You are supposed to enter value from 1 to 3!')


print('Enter the color of multiplier:')
j=input()
mltplrt=mltplr(j)
print(str(mltplrt))
if mltplr_conf:
    resval=int(mltpt)*int(mltplrt)
    if resval>999999:
        resval=resval/1000000
        print('The resistor value is '+str(resval)+' Megaohm(s).')
    elif resval>999:
        resval=resval/1000
        print('The resistor value is '+str(resval)+' Kiloohm(s).')
    else:
        print('The resistor value is '+str(resval)+' ohm(s).')
    
print('Press Enter to quit')
s=input()



