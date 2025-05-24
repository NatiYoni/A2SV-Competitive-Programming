# Problem: Find Pivot Index - https://leetcode.com/problems/find-pivot-index/description/

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        sum_ = sum(nums)
        left = 0

        for i in range(len(nums)):
            

            if (sum_ - nums[i])/2 == left:
                return i

            left += nums[i]

        return -1