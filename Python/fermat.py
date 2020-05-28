''' This is program simulates Fermat's factoring algorithm. 
    It is used to derive factors of a product of two big prime numbers
     which are very close to each other.'''

import math

def fermat(n):
    n=int(n)
    k=int(math.sqrt(n))+1
    d=k**2-n

    while True :
        sqr=math.sqrt(k**2-n)
        if sqr-int(sqr)==0:
            d=k**2-n
            break
        else:
            k+=1
    
    h=math.sqrt(d)

    return k+h, k-h


if __name__=="__main__":
    n=int(input('Enter the product:'))
    a,b=fermat(n)
    print(f"The Primes are: {a} {b}")
