'''https://www.codewars.com/kata/54a91a4883a7de5d7800009c'''

import re
def increment_string(stri):
    num=re.findall(r'[0-9]*$',stri)
    if num==[''] or not stri.endswith(num[-2]):
        return stri+'1'
    else:
        # return re.findall(r'^[a-zA-z]*',stri)[0]+str(int(num[-2])+1).zfill(len(num[-2]))
        return stri[:len(stri)-len(num[-2])]+str(int(num[-2])+1).zfill(len(num[-2]))
