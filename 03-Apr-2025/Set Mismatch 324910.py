# Problem: Set Mismatch - https://leetcode.com/problems/set-mismatch/description/

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        i = 0
        ans = 0
        
        while i < n:
            cur = nums[i] - 1
            # print(nums)

            if cur != i :
                if nums[i] == nums[cur]:
                    ans = nums[i]
                    i += 1
                else:
                    # print(i, nums[i],nums[cur])
                    # return [nums[i], i + 1] if nums[i] <= i else [nums[i], i + 1]
                
                    nums[i], nums[cur] = nums[cur], nums[i]

            else:
                i += 1
        
        for i in range(n):
            if i != nums[i] - 1:
                return [nums[i],i + 1]


