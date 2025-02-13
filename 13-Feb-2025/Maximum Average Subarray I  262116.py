# Problem: Maximum Average Subarray I  - https://leetcode.com/problems/maximum-average-subarray-i/

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        right, left = 0 ,0
        sum = 0
        max_av = float("-inf")

        while right < len(nums):
            sum += nums[right]
            
            if right + 1 >= k:
                max_av = max(max_av, sum)
                sum -= nums[left]
                left += 1
            right += 1
            
        return max_av/k 