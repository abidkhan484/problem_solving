#! /home/polymath/.pyenv/shims/python

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        for i in range(l):
            item = nums[i]
            t = target - item
            j = i+1
            while (j < l):
                if (nums[j] == t):
                    return [i,j]
                j += 1



