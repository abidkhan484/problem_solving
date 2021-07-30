#! /home/polymath/.pyenv/shims/python

from typing import Coroutine


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        currTotal = lastTotal = 0
        left, right = '(', ')'
        stack = []

        for item in s:
            if item is left:
                stack.append(item)
            else:
                if not stack:
                    if currTotal > lastTotal:
                        lastTotal = currTotal
                    currTotal = 0
                else:
                    stack.pop()
                    currTotal += 2

        return lastTotal if lastTotal > currTotal else currTotal
                

parentheses = Solution()
print(parentheses.longestValidParentheses("(()))"))
