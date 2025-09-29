# Problem: Unique Paths - https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        ans = [[0] *(m) for _ in range(n)]
        for i in range(n):
            ans[i][0] = 1
        
        for j in range(m):
            ans[0][j] = 1
        
        for i in range(1,n):
            for j in range(1,m):
                
                ans[i][j] = ans[i][j-1] + ans[i-1][j]
        
        return ans[-1][-1]