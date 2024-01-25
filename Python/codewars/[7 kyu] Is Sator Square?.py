'''https://www.codewars.com/kata/5cb7baa989b1c50014a53333'''

def is_sator_square(tablet):
    x = len(tablet)
    for i in range(0,x):
        for j in range(0,x):
            if tablet[i][j] != tablet[x-i-1][x-j-1]:
                return False
            if tablet[i][j] != tablet[j][i]:
                return False
    return True
        
