# Problem: Subarray Sum Equals K - https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        map_ = {0:1}

        cur = 0
        ans = 0
        for i in range(len(nums)):
            cur += nums[i]

            if (cur - k) in map_:
                ans += map_[cur - k]
            
            if cur in map_:
                map_[cur] += 1

            else:
                map_[cur] = 1
                
        return ans
                
        

        
