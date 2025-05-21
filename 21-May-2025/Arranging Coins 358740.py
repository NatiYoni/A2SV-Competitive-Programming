# Problem: Arranging Coins - https://leetcode.com/problems/arranging-coins/description/

class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        l = 1
        h = n

        while l <= h:

            mid = l + (h - l) // 2

            if (mid *(1 + mid) // 2) <= n:
                l = mid + 1
            
            else:
                h = mid - 1
        
        return h