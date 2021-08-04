#! /home/polymath/.pyenv/shims/python


class Solution:

    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        maxim = 0
        length = len(s)
        for i in range(length):
            if s[i] is '(':
                stack.append(i)
            else:
                stack.pop()
                if (stack):
                    maxim = max(maxim, i-stack[-1])
                else:
                    stack.append(i)

        return maxim


parentheses = Solution()
print(parentheses.longestValidParentheses("(()))"))
