#! /home/polymath/.pyenv/shims/python


class Solution:

    def isValid(self, s:str) -> bool:
        left = '('
        stack = []
        for i in s:
            if i is left:
                stack.append(i)
            elif stack and (stack[-1] is left):
                stack.pop()
            else:
                return False
        return not bool(stack)


    def longestValidParentheses(self, s: str) -> int:
        maxlen = 0
        length = len(s)
        for i in range(0,length):
            for j in range(i+2, length+1, 2):
                if (self.isValid(s[i:j])):
                    maxlen = max(maxlen, j-i)
                
        return maxlen

parentheses = Solution()
print(parentheses.longestValidParentheses("(()))"))
