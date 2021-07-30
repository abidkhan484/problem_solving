#! /home/polymath/.pyenv/shims/python

class Solution:
    def isValid(self, s: str) -> bool:
        status = True
        left_sides = '({['
        right_sides = ')}]'
        
        stack = []
        for item in s:
            if item in left_sides:
                stack.append(item)
            else:
                if not stack:
                    status = False
                    break
                elif right_sides.index(item) == left_sides.index(stack[-1]):
                    stack.pop()
                else:
                    status = False
                    break

        if (stack):
            status = False
        
        
        return status
                    
parentheses = Solution()
print(parentheses.isValid("()"))

