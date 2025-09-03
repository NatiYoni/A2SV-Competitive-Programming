# Problem: Sum of Square Numbers - https://leetcode.com/problems/sum-of-square-numbers/

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for i in range(isqrt(c)+1):
            temp = isqrt(c-i*i)

            if temp*temp == c-i*i:
                return True

        
        return False
            
