# Problem: 132 Pattern - https://leetcode.com/problems/132-pattern/

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
        if len(nums) < 3:
            return False


        # l , r = 0, 2

        # while r < len(nums):
        #     if nums[l] < nums[r] < nums[r-1]:
        #         return True
            
        #     l += 1
        #     r += 1

        # return False

        stack = []
        min_ = nums[0]

        for num in nums:
            
            while stack and stack[-1][0] <= num:
                stack.pop()

            if stack and  num < stack[-1][0]  and stack[-1][1] < num:
                return True
            
            stack.append((num,min_))
            min_ = min(min_,num)

        return False
        