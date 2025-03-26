# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        n = len(weights)
       

        def checker(mid):
            total = 0
            count = 0

            for w in weights:
                total += w

                if total > mid:
                    total = w
                    count += 1
                
            count += 1 if total > 0 else 0 
            return count <= days


        low = max(weights) - 1
        high = sum(weights)

        while low + 1 < high:
            mid = (low + high) // 2
            
            if checker(mid):
                high = mid
            
            else:
                low = mid 
            
        
        return high


