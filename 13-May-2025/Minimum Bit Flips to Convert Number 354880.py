# Problem: Minimum Bit Flips to Convert Number - https://leetcode.com/problems/minimum-bit-flips-to-convert-number/

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        x_  = bin(start)
        y_ = bin(goal)

        
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