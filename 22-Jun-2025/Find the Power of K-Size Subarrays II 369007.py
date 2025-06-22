# Problem: Find the Power of K-Size Subarrays II - https://leetcode.com/problems/find-the-power-of-k-size-subarrays-ii/

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        mx = 0
        n = len(nums)

        if k == 1:
            return nums
            
        ans = []
        l = 0
        for i in range(1,n):
            if nums[i] - nums[i - 1] != 1:
                l = i
            
            if i >= k - 1:
                ans.append(nums[i] if i - l + 1 >= k else -1)
            
        
        return ans
