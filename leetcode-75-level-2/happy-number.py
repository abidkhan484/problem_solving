
class Solution:
    def isHappy(self, n: int) -> bool:
        cycle = []
        number = n
        while number != 1:
            number = 0
            while n:
                number += (n%10) ** 2
                n = n // 10

            if number in cycle:
                break
            cycle.append(number)
            n = number
        
        return True if number==1 else False

