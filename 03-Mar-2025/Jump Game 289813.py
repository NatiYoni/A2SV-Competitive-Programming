# Problem: Jump Game - https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        n = len(nums) - 1
      
        count = -1
        flag = False

        for i in range(n - 1, -1,-1):

            if nums[i] == 0 or flag:
                count += 1
                flag = True
            
            if nums[i] > count and flag:
                count = -1
                flag = False
            
        return not flag

   

