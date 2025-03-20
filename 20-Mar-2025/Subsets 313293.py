# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        arr = []

        def helper(i,temp):
            
            if i >= len(nums):
                arr.append(temp.copy()) 
                return 
            
            temp.append(nums[i])
            helper(i+1, temp)
            temp.pop()
            helper(i+1, temp)
            
        helper(0, [])
        return arr