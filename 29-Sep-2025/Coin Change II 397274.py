# Problem: Coin Change II - https://leetcode.com/problems/coin-change-ii/

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp = [0] * (amount+1)
        # dp[0] = 1
        # for c in coins:
        #     for idx in range(len(dp)):
        #         if c + idx < len(dp):
        #             dp[c + idx] += dp[idx]
        
        # return dp[-1]

        memo = {}
        def recur(i, sm):
            if sm < 0 or i >= len(coins):
                return 0
            
            if sm == 0:
                return 1
            
            if (i,sm) not in memo:
                take = recur(i, sm - coins[i])
                skip = recur(i + 1, sm)

                memo[(i,sm)] = take + skip 
            return memo[(i, sm)]

        
        return recur(0, amount)