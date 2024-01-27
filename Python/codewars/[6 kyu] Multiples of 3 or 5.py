'''https://www.codewars.com/kata/514b92a657cdc65150000006'''

def solution(n):
    if n<=0:
        return 0

    sum = 0 
    
    for i in range(3,n,3):
        sum+=i
    
    for i in range(5,n,5):
        if i%3 != 0:
            sum+=i 
    
    return sum
  
