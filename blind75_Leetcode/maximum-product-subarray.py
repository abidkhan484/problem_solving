from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProduct = -11
        maximum = 1
        minimum = 1
        for num in nums:
            tmpMax = maximum*num
            maximum = max(tmpMax, minimum*num, num)
            minimum = min(tmpMax, minimum*num, num)
            maxProduct = max(maximum, maxProduct)

        return maxProduct

s = Solution()
nums = [-4,-3,-2]
print(s.maxProduct(nums))
