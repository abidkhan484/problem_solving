#! /home/polymath/.pyenv/shims/python

from typing import List

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1_len, num2_len = len(num1), len(num2)
        ans = [0] * (num1_len + num2_len + 1)
        num1, num2 = num1[::-1], num2[::-1]
        for i in range(num1_len):
            p = i
            for j in range(num2_len):
                result = ans[p] + (int(num1[i]) * int(num2[j]))
                ans[p] = result % 10
                ans[p+1] += result // 10
                p += 1
        ans.reverse()
        ans = ''.join(map(str, ans))
        ans = ans.lstrip('0')
        return ans if ans else '0'


num1 = "0"; num2 = "0"
s = Solution()
answer = s.multiply(num1, num2)
print(answer)
