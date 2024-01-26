'''https://leetcode.com/problems/two-sum'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}
        for i in range(len(nums)):
            dic[nums[i]]=i
        
        for i in range(len(nums)):
            dif = target-nums[i]
            if dif in dic.keys():
                if dic[dif] == i:
                    continue
                return [i,dic[dif]]
