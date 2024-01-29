'''https://www.codewars.com/kata/5208f99aee097e6552000148'''

def solution(s):
    return "".join([" "+i if i.isupper() else i for i in s])
