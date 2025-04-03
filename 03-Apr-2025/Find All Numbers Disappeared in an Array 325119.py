# Problem: Find All Numbers Disappeared in an Array - https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        i = 0
        n = len(nums)
        # rep = -1

        while i < n:
            # print(nums)
            cur = nums[i] - 1
            if cur != i:
                if nums[i] == nums[cur]:
                    
                    i += 1
                else:
                    nums[i], nums[cur] = nums[cur],nums[i]
            
            else:
                i += 1

        # print(nums)
        output = []
        for i in range(n):
            if i + 1 != nums[i]:
                output.append(i + 1)
        return output