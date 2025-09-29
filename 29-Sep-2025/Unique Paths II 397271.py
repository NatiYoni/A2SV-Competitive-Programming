# Problem: Unique Paths II - https://leetcode.com/problems/unique-paths-ii/

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # direction = [(0,1), (1,0)]
        n = len( obstacleGrid)
        m = len( obstacleGrid[0])

        ans = [[0] *(m) for _ in range(n)]
        for i in range(n):
            if obstacleGrid[i][0] == 0:
                ans[i][0] = 1
            else:
                break
        
        for j in range(m):
            if obstacleGrid[0][j] == 0:
                ans[0][j] = 1
            else:
                break



        for i in range(1,n):
            for j in range(1,m):
                if  obstacleGrid[i][j] == 0:
                    ans[i][j] = ans[i-1][j] + ans[i][j-1]
        
        # print(ans)
        return ans[n-1][m-1] 
