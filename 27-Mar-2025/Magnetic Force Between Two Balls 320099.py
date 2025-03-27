# Problem: Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        
        position.sort()

        def checker(mid):
            count = 1
            prev = 0

            for i in range(1,len(position)):
                if position[i] - position[prev] >= mid:
                    prev = i
                    count += 1
            return  count >= m

          
        
        low = 1
        high = max(position)
        ans = 0

        while low <= high:
            mid = (low + high) // 2

            if checker(mid):
                low = mid + 1
                ans = mid
            
            else:
                high = mid - 1

        return ans
        