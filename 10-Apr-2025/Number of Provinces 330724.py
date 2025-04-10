# Problem: Number of Provinces - https://leetcode.com/problems/number-of-provinces/

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        cols = len(isConnected)
        rows = len(isConnected[0])
        count = 0

        def dfs(row):
            if isConnected[row][row] == 0:
                return

            # isConnected[row][row] == 0
            for col in range(cols):
                if isConnected[row][col] == 1:
                    isConnected[row][col] = 0
                    isConnected[col][row] = 0

                    dfs(col)
            
        for i in range(rows):
            
            if isConnected[i][i] == 1:
                count += 1
                dfs(i)
        
        return count
