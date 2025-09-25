# Problem: Partition Equal Subset Sum - https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sm = sum(nums)
        if sm % 2 == 1:
            return False

        memo = {}
        def recur(i,val,sm):

            if i == len(nums) or val > sm // 2:
                return False
            
            if (val,i) in memo:
                return memo[(val, i)]

            if sm - val == val:
                return True
            
            memo[(val,i)] = False

            flag = recur(i+1,val+nums[i],sm) or recur(i+1, val, sm)

            return flag
            
        
        return recur(0,0,sm)

