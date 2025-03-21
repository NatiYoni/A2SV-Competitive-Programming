# Problem: Permutations - https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        arr = []

        def backtracker(index,temp):

            if len(temp) == len(nums):
                arr.append(temp.copy())
                return            
            
            for i in range(index, len(nums)):
                if nums[i] not in temp:
                    temp.append(nums[i])
                    backtracker(index, temp)
                    temp.pop()
            
        backtracker(0,[])
        return arr