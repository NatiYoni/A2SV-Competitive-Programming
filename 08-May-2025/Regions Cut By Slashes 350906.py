# Problem: Regions Cut By Slashes - https://leetcode.com/problems/regions-cut-by-slashes/description/

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        
        represent = [[0] * len(grid)* 3 for _ in range(len(grid) * 3) ]
        for i in range(len(grid)):
            for j in range(len(grid)):

                row = i * 3
                col = j * 3
                if grid[i][j] == "/":
                    represent[row][col + 2] = represent[row + 1][col + 1] = represent[row + 2][col] = 1
                elif grid[i][j] == "\\":
                    represent[row][col]  = represent[row + 1][col + 1] = represent[row + 2][col + 2] = 1
        
        # print(represent)


        # using dfs

        def inbound(row,col):
            return 0 <= row < len(represent) and 0 <= col < len(represent)

        direction = [(1,0),(0,1),(-1,0),(0,-1)]

        def dfs(row,col):
            
            represent[row][col] = 1
            for x,y in direction:
                nr = row + x
                nc = col + y

                if inbound(nr,nc) and  represent[nr][nc] == 0:
                    dfs(nr,nc) 
                    # print(represent)

        count = 0
        for i in range(len(represent)):
            for j in range(len(represent)):
                if represent[i][j] == 0:
                    count += 1
                    dfs(i,j)
                    # print(represent)
        
        return count



































        # parent = [[i + j for i in range(len(grid))] for j in range(len(grid))]
        # print(parent)
        # def find(x):
        #     while parent[x] != x:
        #         parent[x] = parent[parent[x]]
        #         x = parent[x]

        #     return parent[x]
        
        # def union(x,y):
        #     x_ = find(x)
        #     y_ = find(y)
            

        #     if x_ != y_:
        #         parent[x_] = y_

        
