# Problem: Pow (x, n) - https://leetcode.com/problems/powx-n/

class Solution:
  
    def myPow(self, x: float, n: int) -> float:

        if n == 0:
            return 1

        temp = self.myPow(x, abs(n) // 2)
        result = temp * temp

        if abs(n) % 2 != 0:
            result *= x
            
        return result if n > 0 else 1 / result