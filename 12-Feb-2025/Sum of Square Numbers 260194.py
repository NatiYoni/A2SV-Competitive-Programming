# Problem: Sum of Square Numbers - https://leetcode.com/problems/sum-of-square-numbers/

class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        a, b = 0 , int(sqrt(c))
        while a <= b:
            if a**2 + b**2 == c:
                return True
            elif a**2 + b**2 > c:
                b -= 1
            else:
                a += 1

        return False   
            
             