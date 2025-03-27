# Problem: Maximum Candies Allocated to K Children - https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        
        if sum(candies) < k:
            return 0

        def checker(mid):
            count = 0
            for candie in candies:
                if candie >= mid:
                    count += candie // mid if mid > 0 else 0
            
            return  count >= k

            pass
        
        low = 1
        high = max(candies)

        while low <= high:

            mid = (high + low) // 2
            

            if checker(mid):
                low = mid + 1
                
            else:
                high = mid - 1 
                pass
        
        return  high 

        # total = sum(candies)
        # ans = total // k
        # min_ = min(candies)
        # # print(7//4)
        
        # return ans if ans < min_ else min_
