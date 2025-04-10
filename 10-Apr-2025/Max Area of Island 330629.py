# Problem: Max Area of Island - https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        directions = [(-1,0),(0,1),(0,-1),(1,0)]
        cols = len(grid[0])
        rows = len(grid)
        # mat = [[-1] * cols for i in range(rows)]
        island = 0


        # print(mat)
        def dfs(row,col):
            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == 0:
                return 0
            
            grid[row][col] = 0
            area = 1
            for x, y in directions: 
                new_row = row + x
                new_col = col + y
                area += dfs(new_row,new_col)
            
            return area

        max_area = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    max_area = max(dfs(i,j),max_area)

        return max_area
        
