# Problem: Minimum Operations to Exceed Threshold Value II - https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        heapify(nums)

        ans = 0
        while nums[0] < k:
            ans += 1
            val1 = heappop(nums)
            val2 = heappop(nums)

            new_val = min(val1,val2) * 2 + max(val1,val2) 
            heappush(nums,new_val)
        
        return ans