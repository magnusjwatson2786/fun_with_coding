'''
Problem at: https://leetcode.com/problems/roman-to-integer/
'''

class Solution:
    def romanToInt(self, s: str) -> int:
        d={
            'CM':900,
            'CD':400,
            'XC':90, 
            'XL':40, 
            'IX':9, 
            'IV':4, 
            'I':1, 
            'V':5, 
            'X':10, 
            'L':50, 
            'C':100,
            'D':500,
            'M':1000
        }
        pos=0
        n=0
        while True:
            if not s[pos:]:
                break
            for i in d.keys():
                if s[pos:].startswith(i):
                    n+=d[i]
                    pos+=len(i)
        return n
