# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        map_ = {0:1}

        cur = 0
        ans = 0
        for i in range(len(nums)):
            cur += nums[i]
            
            if (cur % k) in map_:
                
                ans += map_[cur % k]
                
            
            if (cur % k)  in map_:
                map_[cur % k] += 1

            else:
                map_[cur % k] = 1
        
        return ans