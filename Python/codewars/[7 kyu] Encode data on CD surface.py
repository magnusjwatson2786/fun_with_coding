'''https://www.codewars.com/kata/643a47fadad36407bf3e97ea'''

def encode_cd(n):
    rb = bin(n)[:1:-1]
    rb = rb + '0'*(8-len(rb))
    pl=['P']
    for i in rb:
        if int(i)==1:
            if pl[-1]=='P':
                pl.append('L')
            else:
                pl.append('P')
        else:
            pl.append(pl[-1])
    return "".join(pl)
