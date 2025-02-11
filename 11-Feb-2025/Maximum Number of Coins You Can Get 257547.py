# Problem: Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        
        n = len(piles)
        start = n // 3
        result = 0

        for index in range(start, n, 2):
            result += piles[index]
        
        return result