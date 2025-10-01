# Problem: Edit Distance - https://leetcode.com/problems/edit-distance/description/

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        if m == 0:
            return n
        
        elif n == 0:
            return m


        dp = [[0] * (m+1) for _ in range(n+1)]
        for i in range(1,m+1):
            dp[0][i] = i
        
        for i in range(1,n+1):
            dp[i][0] = i

        for i in range(1,n+1):
            for j in range(1,m+1):
                if word1[j-1] == word2[i-1]:
                    dp[i][j] =  dp[i-1][j-1]
                
                else:
                    dp[i][j] = min(dp[i - 1][j] , dp[i][j - 1] , dp[i-1][j-1]) + 1
           
        # print(dp)
        return dp[-1][-1] 


        # memo = {}
        # def recur(i,j):
        #     if i == n or  j == m:
        #         return max(n-i,m-j)
            
        #     if (i,j) not in memo:
        #         ans = 0
        #         if word1[j] == word2[i]:
        #             ans = recur(i+1,j+1)
                
        #         else:
        #             ans = min(recur(i + 1, j) , recur(i, j + 1) , recur(i+1,j+1)) + 1
        #         memo[(i,j)] = ans
                
        #     return memo[(i,j)]
        
        
        # return recur(0,0)