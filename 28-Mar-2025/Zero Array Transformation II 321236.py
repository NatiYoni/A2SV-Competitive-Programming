# Problem: Zero Array Transformation II - https://leetcode.com/problems/zero-array-transformation-ii/

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        

        if all(x == 0 for x in nums):
            return 0

        def checker(mid):

            ans = nums.copy()
            prefix = [0] * (len(nums) + 2)

            for i in range(mid) :

                start, end, val = queries[i]
                prefix[start] -= val

                if end + 1 < len(nums):
                    prefix[end + 1] += val
            
            for i in range(1,len(nums)):
                prefix[i]  += prefix[i-1] 
            
            
            for i in range(len(nums)):
              
                ans[i] += prefix[i]
                
                if ans[i] > 0:  
                    return False

            return True


        left = 0
        right = len(queries) + 1

        while left + 1 < right:
            mid = (left + right) // 2
        
            if checker(mid):
                right = mid
                
            else:
                left = mid

        
        return right if right <= len(queries) and checker(right) else -1

        # for i in range(len(nums)):
        #     nums[i] += prefix[i]
            
        
        # print(nums)

        # min_ =  float("inf")
        # count = 0
        # for i in range(len(nums)):

        #     if nums[i] >= 0 and nums[i] < min_:
        #         min_ = nums[i]
        #         count = 1
            
        #     elif min_ == nums[i]:
        #         count += 1
        
        # return count if count > 0 else -1