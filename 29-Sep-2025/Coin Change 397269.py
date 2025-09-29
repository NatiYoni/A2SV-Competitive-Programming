# Problem: Coin Change - https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # if amount == 0:
        #     return 0

        n = len(coins)
        dp = [math.inf] * (amount + 1)
        dp[0] = 0
        for i in range(n):
            for j in range(amount+1):
                if j - coins[i] >= 0:
                    dp[j] =   min(dp[j-coins[i]] + 1,dp[j])

        # print(dp)
        return dp[amount]  if dp[amount] != math.inf else -1

    