'''https://www.codewars.com/kata/5526fc09a1bbd946250002dc'''

def find_outlier(il):
    is_even=0
    if il[0]%2==0:
        if il[1]%2==0:
            is_even=1
        else:
            if il[2]%2==0:
                is_even=1
    else:
        if il[0]%2!=0:
            if il[1]%2==0:
                if il[2]%2==0:
                    is_even=1

    if is_even:
        for i in il:
            if i%2!=0:
                return i
    else:
        for i in il:
            if i%2==0:
                return i
