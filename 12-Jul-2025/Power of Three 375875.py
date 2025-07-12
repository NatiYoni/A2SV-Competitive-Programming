# Problem: Power of Three - https://leetcode.com/problems/power-of-three/

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        def pow(n):
            if n == 3 or n == 1:
                return True
            
            if n < 3 or n % 3 != 0:
                return False
            
            flag = pow(n/3)
            return flag
        
        return pow(n)