from math import*
from sys import*
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>CYBORG ULTRA<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
print('<<<<<<<<<<<<<<<<<<<<<<Welcome to Scientific Calculator>>>>>>>>>>>>>>>>>>>>>>')
continu=1
while continu==1:
    used=0
    print('Enter 1 for addition')
    print('Enter 2 for subtraction')
    print('Enter 3 for multiplication')
    print('Enter 4 for division')
    print('Enter 5 for Remainder')
    print('Enter 6 for GCD')
    print('Enter 7 for Factorial')
    print('Enter 8 for Square root')
    print('Enter 9 for Exponential Multiplication')
    print('Enter 10 for Euclidean Distance')
    print('Enter 11 for natural logarithm')
    print('Enter 12 for logarithm(base 10)')
    print('Enter 13 for logarithm(base 2)')
    print('Enter 14 for sine')
    print('Enter 15 for cosine')
    print('Enter 16 for tangent')
    print('Enter 17 for cosecant')
    print('Enter 18 for secant')
    print('Enter 19 for cotangent')
    print('Enter 20 for sine inverse')
    print('Enter 21 for cosine inverse')
    print('Enter 22 for tangent inverse')
    print('Enter 23 for radian-to-degree conversion')
    print('Enter 24 for degree-to-radian conversion')
    print('Enter 0 to quit')
    choice=input()
    if int(choice)==14:
        used=1
        rpt1=1
        while rpt1==1:
            print('Sine Calculation')
            auth1=False
            while auth1== False:
                print('Enter 1  for angle in radians or 2 for angle in degrees')
                choice1=input()
                if int(choice1)==2:      
                    print('Enter the measure of angle in degrees')
                    x=input()
                    print('Required Value: '+str(sin(radians(float(x)))))
                    auth1=True
                elif int(choice1)==1:      
                    print('Enter the measure of angle in radians')
                    x=input()
                    print('Required Value: '+str(sin(float(x))))
                    auth1=True
                else:
                    print('Invalid Value.Retry')
                    auth1=False
            print('press y for more like these or press any key to return to the main menu')
            rpch=input()
            if rpch=='y':
                print('lets start again.')
            else:
                rpt1=0
    elif int(choice)==15:
        used=1
        rpt1=1
        while rpt1==1:
            print('Cosine Calculation')
            auth1=False
            while auth1== False:
                print('Enter 1  for angle in radians or 2 for angle in degrees')
                choice1=input()
                if int(choice1)==2:      
                    print('Enter the measure of angle in degrees')
                    x=input()
                    print('Required Value: '+str(cos(radians(float(x)))))
                    auth1=True
                elif int(choice1)==1:      
                    print('Enter the measure of angle in radians')
                    x=input()
                    print('Required Value: '+str(cos(float(x))))
                    auth1=True
                else:
                    print('Invalid Value.Retry')
                    auth1=False
            print('press y for more like these or press any key to return to the main menu')
            rpch=input()
            if rpch=='y':
                print('lets start again.')
            else:
                rpt1=0
    elif int(choice)==16:
        used=1
        rpt1=1
        while rpt1==1:
            print('Tangent Calculation')
            auth1=False
            while auth1== False:
                print('Enter 1  for angle in radians or 2 for angle in degrees')
                choice1=input()
                if int(choice1)==2:      
                    print('Enter the measure of angle in degrees')
                    x=input()
                    print('Required Value: '+str(tan(radians(float(x)))))
                    auth1=True
                elif int(choice1)==1:      
                    print('Enter the measure of angle in radians')
                    x=input()
                    print('Required Value: '+str(tan(float(x))))
                    auth1=True
                else:
                    print('Invalid Value.Retry')
                    auth1=False
            print('press y for more like these or press any key to return to the main menu')
            rpch=input()
            if rpch=='y':
                print('lets start again.')
            else:
                rpt1=0
    elif int(choice)==20:
        used=1
        rpt1=1
        while rpt1==1: 
            print('Sine Inverse Calculation')
            print('Enter the Value:')
            x=input()
            print('Required Angle (in radians): '+str(asin(float(x))))
            print('Required Angle (in degrees): '+str(degrees(asin(float(x)))))
            print('press y for more like these or press any key to return to the main menu')
            rpch=input()
            if rpch=='y':
                print('lets start again.')
            else:
                rpt1=0
    elif int(choice)==21:
        used=1
        rpt1=1
        while rpt1==1:
            print('Cosine Inverse Calculation')
            print('Enter the Value:')
            x=input()
            print('Required Angle (in radians): '+str(acos(float(x))))
            print('Required Angle (in degrees): '+str(degrees(acos(float(x)))))
            print('press y for more like these or press any key to return to the main menu')
            rpch=input()
            if rpch=='y':
                print('lets start again.')
            else:
                rpt1=0
    elif int(choice)==22:
        used=1
        rpt1=1
        while rpt1==1:
            print('Tangent Inverse Calculation')
            print('Enter the Value:')
            x=input()
            print('Required Angle (in radians): '+str(atan(float(x))))
            print('Required Angle (in degrees): '+str(degrees(atan(float(x)))))
            print('press y for more like these or press any key to return to the main menu')
            rpch=input()
            if rpch=='y':
                print('lets start again.')
            else:
                rpt1=0
    elif int(choice)==23:
        used=1
        rpt1=1
        while rpt1==1:
            print('Radian-to-Degree Conversion')
            print('Enter the angle in radians:')
            x=input()
            print('Required Angle in degrees: '+str(degrees(float(x))))
            print('press y for more like these or press any key to return to the main menu')
            rpch=input()
            if rpch=='y':
                print('lets start again.')
            else:
                rpt1=0
    elif int(choice)==24:
        used=1
        rpt1=1
        while rpt1==1:
            print('Degree-to-Radian Conversion')
            print('Enter the angle in degrees:')
            x=input()
            print('Required Angle in radians: '+str(radians(float(x))))
            print('press y for more like these or press any key to return to the main menu')
            rpch=input()
            if rpch=='y':
                print('lets start again.')
            else:
                rpt1=0
    elif int(choice)==11:
        used=1
        rpt1=1
        while rpt1==1:
            print('Natural Logarithm')
            print('Enter the value of argument:')
            x=float(input())
            print('Enter the value of base:')
            print('If the base not specified, returns the natural logarithm (base e) of x.')
            y=input()
            if y:
                q=float(y)
                print('Required Value: '+str(log(x,q)))
            else:
                print('Required Value: '+str(log(x)))
            print('press y for more like these or press any key to return to the main menu')
            rpch=input()
            if rpch=='y':
                print('lets start again.')
            else:
                rpt1=0
    elif int(choice)==12:
        used=1
        rpt1=1
        while rpt1==1:
            print('Logarithm(base 10)')
            print('Enter the value of argument:')
            x=input()
            print('Required Value: '+str(log10(float(x))))
            print('press y for more like these or press any key to return to the main menu')
            rpch=input()
            if rpch=='y':
                print('lets start again.')
            else:
                rpt1=0
    elif int(choice)==13:
        used=1
        rpt1=1
        while rpt1==1:
            print('Logarithm(base 2)')
            print('Enter the value of argument::')
            x=input()
            print('Required Value: '+str(log2(float(x))))
            print('press y for more like these or press any key to return to the main menu')
            rpch=input()
            if rpch=='y':
                print('lets start again.')
            else:
                rpt1=0
    elif int(choice)==17:
        used=1
        rpt1=1
        while rpt1==1:
            print('Cosecant Calculation')
            auth1=False
            while auth1== False:
                print('Enter 1  for angle in radians or 2 for angle in degrees')
                choice1=input()
                if int(choice1)==2:      
                    print('Enter the measure of angle in degrees')
                    x=input()
                    print('Required Value: '+str(1/(sin(radians(float(x))))))
                    auth1=True
                elif int(choice1)==1:      
                    print('Enter the measure of angle in radians')
                    x=input()
                    print('Required Value: '+str(1/(sin(float(x)))))
                    auth1=True
                else:
                    print('Invalid Value.Retry')
                    auth1=False
            print('press y for more like these or press any key to return to the main menu')
            rpch=input()
            if rpch=='y':
                print('lets start again.')
            else:
                rpt1=0
    elif int(choice)==18:
        used=1
        rpt1=1
        while rpt1==1:
            print('Secant Calculation')
            auth1=False
            while auth1== False:
                print('Enter 1  for angle in radians or 2 for angle in degrees')
                choice1=input()
                if int(choice1)==2:      
                    print('Enter the measure of angle in degrees')
                    x=input()
                    print('Required Value: '+str(1/(cos(radians(float(x))))))
                    auth1=True
                elif int(choice1)==1:      
                    print('Enter the measure of angle in radians')
                    x=input()
                    print('Required Value: '+str(1/(cos(float(x)))))
                    auth1=True
                else:
                    print('Invalid Value.Retry')
                    auth1=False
            print('press y for more like these or press any key to return to the main menu')
            rpch=input()
            if rpch=='y':
                print('lets start again.')
            else:
                rpt1=0
    elif int(choice)==19:
        used=1
        rpt1=1
        while rpt1==1:
            print('Cotangent Calculation')
            auth1=False
            while auth1== False:
                print('Enter 1  for angle in radians or 2 for angle in degrees')
                choice1=input()
                if int(choice1)==2:      
                    print('Enter the measure of angle in degrees')
                    x=input()
                    print('Required Value: '+str(1/(tan(radians(float(x))))))
                    auth1=True
                elif int(choice1)==1:      
                    print('Enter the measure of angle in radians')
                    x=input()
                    print('Required Value: '+str(1/(tan(float(x)))))
                    auth1=True
                else:
                    print('Invalid Value.Retry')
                    auth1=False
            print('press y for more like these or press any key to return to the main menu')
            rpch=input()
            if rpch=='y':
                print('lets start again.')
            else:
                rpt1=0
    elif int(choice)==9:
        used=1
        rpt1=1
        while rpt1==1:
            print('Exponential Multiplication')
            print('Enter base:')
            x=float(input())
            print('Enter Exponent:')
            y=int(input())
            print('Required Value: '+str(pow(x,y)))
            print('press y for more like these or press any key to return to the main menu')
            rpch=input()
            if rpch=='y':
                print('lets start again.')
            else:
                rpt1=0
    elif int(choice)==8:
        used=1
        rpt1=1
        while rpt1==1:
            print('Square Root')
            print('Enter the number:')
            x=input()
            print('Required Value: '+str(sqrt(float(x))))
            print('press y for more like these or press any key to return to the main menu')
            rpch=input()
            if rpch=='y':
                print('lets start again.')
            else:
                rpt1=0
    elif int(choice)==7:
        used=1
        rpt1=1
        while rpt1==1:
            print('Factorial!')
            print('Enter the number:')
            x=input()
            print('Required Value: '+str(factorial(int(x))))
            print('press y for more like these or press any key to return to the main menu')
            rpch=input()
            if rpch=='y':
                print('lets start again.')
            else:
                rpt1=0
    elif int(choice)==5:
        used=1
        rpt1=1
        while rpt1==1:   
            print('Remainder')
            print('Enter dividend:')
            x=input()
            print('Enter divisor:')
            y=input()
            print('Required Value: '+str((int(x))%(int(y))))
            print('press y for more like these or press any key to return to the main menu')
            rpch=input()
            if rpch=='y':
                print('lets start again.')
            else:
                rpt1=0
    elif int(choice)==6:
        used=1
        rpt1=1
        while rpt1==1:
            print('Greatest Common Divisor')
            print('Enter 1st no.:')
            x=int(input())
            print('Enter 2nd no.:')
            y=int(input())
            print('Required GCD: '+str(gcd(x,y)))
            print('press y for more like these or press any key to return to the main menu')
            rpch=input()
            if rpch=='y':
                print('lets start again.')
            else:
                rpt1=0
    elif int(choice)==10:
        used=1
        rpt1=1
        while rpt1==1:
            print('Hypotenuse')
            print('Enter Perpendicular:')
            x=float(input())
            print('Enter Base:')
            y=float(input())
            print('Required Hypotenuse: '+str(hypot(x,y)))
            print('press y for more like these or press any key to return to the main menu')
            rpch=input()
            if rpch=='y':
                print('lets start again.')
            else:
                rpt1=0
    elif int(choice)==1:
        used=1
        rpt1=1
        while rpt1==1:
            print('Addition')
            print('Enter 1st no.:')
            x=float(input())
            print('Enter 2nd no.:')
            y=float(input())
            print('Required Value: '+str(x+y))
            print('press y for more like these or press any key to return to the main menu')
            rpch=input()
            if rpch=='y':
                print('lets start again.')
            else:
                rpt1=0
    elif int(choice)==2:
        used=1
        rpt1=1
        while rpt1==1:
            print('Subtraction')
            print('Enter 1st no.:')
            x=float(input())
            print('Enter 2nd no.:')
            y=float(input())
            print('Required Value: '+str(x-y))
            print('press y for more like these or press any key to return to the main menu')
            rpch=input()
            if rpch=='y':
                print('lets start again.')
            else:
                rpt1=0
    elif int(choice)==3:
        used=1
        rpt1=1
        while rpt1==1:
            print('Multiplication')
            print('Enter 1st no.:')
            x=float(input())
            print('Enter 2nd no.:')
            y=float(input())
            print('Required Value: '+str(x*y))
            print('press y for more like these or press any key to return to the main menu')
            rpch=input()
            if rpch=='y':
                print('lets start again.')
            else:
                rpt1=0
    elif int(choice)==4:
        used=1
        rpt1=1
        while rpt1==1:
            print('Division')
            print('Enter Dividend:')
            x=float(input())
            print('Enter Divisor:')
            y=float(input())
            print('Required Value: '+str(x/y))
            print('press y for more like these or press any key to return to the main menu')
            rpch=input()
            if rpch=='y':
                print('lets start again.')
            else:
                rpt1=0
    elif int(choice)==0:
        exit()
    else:
        print('Invalid Value.Retry')
    if used==1:
        print('press y for more Calculations or press any key to exit')
        cont=input()
        if cont=='y':
            print('lets start again.')
        else:
            continu=0
