# Problem: Binary Subarrays With Sum - https://leetcode.com/problems/binary-subarrays-with-sum/

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        map_ = defaultdict(int)
        map_[0] = 1
        
        result = cur = 0
        for num in nums:
            cur += num
            result += map_[cur - goal]
            map_[cur] += 1
            

        return result