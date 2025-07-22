# Problem: Maximum Erasure Value  - https://leetcode.com/problems/maximum-erasure-value/

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen = set()
        ans = 0
        l = 0
        temp = 0

        for val in nums:
            while l < len(nums) and val in seen:
                temp -= nums[l]
                seen.discard(nums[l])
                l += 1
            
            seen.add(val)
            temp += val
            ans = max(temp,ans)

        return ans
                