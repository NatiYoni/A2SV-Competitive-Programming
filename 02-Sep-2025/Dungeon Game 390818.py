# Problem: Dungeon Game - https://leetcode.com/problems/dungeon-game/

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:

        m = len(dungeon[0])
        n = len(dungeon)
        dp = [[0] * (m+1) for _ in range(n+1)]

        for i in range(n-1,-1,-1):
            dp[i][m-1] = min(dp[i+1][m-1] + dungeon[i][m-1], dungeon[i][m-1])
        
        for j in range(m-1,-1,-1):
            dp[n-1][j] = min(dp[n-1][j+1] + dungeon[n-1][j], dungeon[n-1][j],)
  
        for i in range(n-2,-1,-1):
            for j in range(m-2,-1,-1):
                prevMx = max(dp[i+1][j],dp[i][j+1])
                cur = dungeon[i][j]

                dp[i][j] = min(cur, prevMx + cur)

        return abs(dp[0][0])  + 1 if dp[0][0] <= 0 else 1

