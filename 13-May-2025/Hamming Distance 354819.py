# Problem: Hamming Distance - https://leetcode.com/problems/hamming-distance/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
    
        x_  = bin(x)
        y_ = bin(y)

        
        l1 = len(x_) - 1
        l2 = len(y_) - 1
        ans = 0

        while l1 > 1 and l2 > 1:
            if x_[l1] != y_[l2]:
                ans += 1
            
            l1 -= 1
            l2 -= 1
        
        while l1 > 1:
            if x_[l1] != "0":
                ans += 1
            l1-= 1
            
        while l2 > 1:
            if y_[l2] != "0":
                ans += 1
            l2 -= 1

        return ans 
