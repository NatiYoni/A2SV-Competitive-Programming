# Problem: Target Sum - https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        sm = sum(nums)
        n = len(nums)

        if sm < target or -sm > target:
            return 0

        dp = [[0] *(2 * sm + 1) for _ in range(n+1)]

        dp[-1][target + sm ] = 1

        target += sm

        for i in range(n-1,-1,-1):
            for j in range(2*sm+1):
                
                if (j - nums[i] >= 0) and (j + nums[i] < 2*sm+1):
                    dp[i][j] = dp[i+1][j + nums[i]] + dp[i+1][j - nums[i]]

        return dp[0][sm]

        # memo = {}
        # def dp(i,sm):
        #     if sm == target and i==len(nums):
        #         return 1
                
        #     if i >= len(nums):
        #         return 0
            
        #     if (i,sm) not in memo:
        #         memo[(i,sm)] = dp(i+1, sm + nums[i]) + dp(i+1,sm - nums[i])

        #     return memo[(i,sm)]
        
        # return dp(0,0)