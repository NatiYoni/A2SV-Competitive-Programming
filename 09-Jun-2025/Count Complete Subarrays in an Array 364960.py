# Problem: Count Complete Subarrays in an Array - https://leetcode.com/problems/count-complete-subarrays-in-an-array/

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        
        hash = defaultdict(int)
        whole = set(nums)
        sub = defaultdict(int)

        ans = 0
        l = 0
        for i,num in enumerate(nums):

            sub[num] += 1
            
            while len(sub) == len(whole) and l < len(nums):
                # print(len(nums),l)
                ans += len(nums) - i

                sub[nums[l]] -= 1
                if sub[nums[l]] == 0:
                    del sub[nums[l]]
                l += 1

        return ans 
            
            
