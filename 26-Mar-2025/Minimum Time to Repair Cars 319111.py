# Problem: Minimum Time to Repair Cars - https://leetcode.com/problems/minimum-time-to-repair-cars/

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:

        def checker(mid):
            count = 0
            for rank in ranks:
                count += floor(sqrt(mid//rank)) 
            
            return count

        
        low = 1
        high = max(ranks) * (cars ** 2)


        while low <= high :

            mid = (low + high) // 2

            if checker(mid) >= cars:
            
                high = mid - 1
            
            else:
                low = mid + 1
        
        return high + 1