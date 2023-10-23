'''
Problem at : https://leetcode.com/problems/power-of-four/
'''
from math import log
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=0: return False
        return True if str(log(n,4)).endswith('.0') else False
