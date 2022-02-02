#! /home/polymath/.pyenv/shims/python
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        answer = []
        # initializing 1 to multiply by first and last number
        leftProds = [1]
        rightProds = [1]

        curLeftProd = 1
        curRightProd = 1
        for i in range(length):
            curLeftProd *= nums[i]
            curRightProd *= nums[length-i-1]
            leftProds.append(curLeftProd)
            rightProds.append(curRightProd)
        rightProds.pop()

        for i in range(length):
            production = leftProds[i] * rightProds[length-i-1]
            answer.append(production)

        return answer


s = Solution()
nums = [-1,1,0,-3,3]
answer = s.productExceptSelf(nums)
print(answer)
