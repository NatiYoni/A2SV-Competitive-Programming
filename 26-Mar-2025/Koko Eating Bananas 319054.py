# Problem: Koko Eating Bananas - https://leetcode.com/problems/koko-eating-bananas/

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def checker(mid):
            count = 0

            for pile in piles:

                count += ceil(pile / mid)
            return count <= h

        low = 0
        high = max(piles)

        while low + 1 < high:
            mid = (low + high) // 2

            if checker(mid):
                high = mid
            
            else:
                low = mid


        return high
