# Problem: Power of Four - https://leetcode.com/problems/power-of-four/

class Solution:
    def isPowerOfFour(self, n: int) -> bool:

        if n == 1: 
            return True

        elif n < 1:
            return False

        return self.isPowerOfFour(n/4)
    
        # def check(n):

        #     if n == 1:
        #         return True
        #     elif n < 1:
        #         return False
            
        #     return check(n/4)
        
        # return check(n)
       
     