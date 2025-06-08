# Problem: Count Subarrays Where Max Element Appears at Least K Times - https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        
        mx = max(nums)
        print(mx)

        ans = 0
        count = 0
        l = 0
        for i in range(len(nums)):
            if nums[i] == mx:
                count += 1
            while count >= k:
                
                if nums[l] == mx:
                    count -= 1

                l += 1

            ans += l

        return ans