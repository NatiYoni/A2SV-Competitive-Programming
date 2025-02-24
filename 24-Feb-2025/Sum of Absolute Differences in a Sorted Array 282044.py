# Problem: Sum of Absolute Differences in a Sorted Array - https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/

class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:

        prefix = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            prefix[i + 1] = prefix[i] + nums[i]
        
        result = []
        
        for i in range(len(nums)):
            ans = (nums[i] * i - prefix[i]) + (prefix[len(nums)] - prefix[i + 1]) - nums[i] * (len(nums) - i - 1)
            result.append(ans)
        
        return result

