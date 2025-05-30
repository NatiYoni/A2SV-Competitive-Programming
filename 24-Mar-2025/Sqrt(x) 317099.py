# Problem: Sqrt(x) - https://leetcode.com/problems/sqrtx/

class Solution:
    def mySqrt(self, x: int) -> int:

        left = 0
        right = x

        while left <= right:
            mid  = (right+ left) // 2 
            if mid * mid > x:
                right = mid - 1
            
            elif mid * mid < x:
                left = mid + 1
            
            else:
                return mid
        
        return right
        



        