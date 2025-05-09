# Problem: Check if There is a Valid Path in a Grid - https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:

        parent = {}
        size = {}

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                parent[(i,j)] = (i,j)
                size[(i,j)] = 1

        

        def find(x):
            
            while parent[x] != x:
                parent[x] = parent[parent[x]] 
                x = parent[x]
            return x

        def union(x, y):
            x_ = find(x)
            y_ = find(y)
            if x_ != y_:
                if size[x_]< size[y_]:
                    x_, y_ = y_, x_
                    
                parent[y_] = x_
                size[x_]+= size[y_]
        
        path = {

            (1,(0,1)) : {1,3,5},
            (1,(0,-1)) : {1,4,6},
            (2,(1,0)) : {2,5,6},
            (2,(-1,0)) : {2,3,4},
            (3,(0,-1)) : {1,4,6},
            (3,(1,0)) : {2,5,6},
            (4,(0,1)) : {1,3,5},
            (4,(1,0)) : {2,5,6},
            (5,(0,-1)) : {1,4,6},
            (5,(-1,0)) : {2,3,4},
            (6,(0,1)) : {1,3,5},
            (6,(-1,0)) : {2,3,4}

        }

        direction = {
            1 : [(0,1),(0,-1)],
            2 : [(1,0),(-1,0)],
            3 : [(0,-1), (1,0)],
            4 : [(0,1), (1,0)],
            5 : [(0,-1),(-1,0)],
            6 : [(-1,0),(0,1)],
        }
        

        def inbound(i,j):
            return 0 <= i < len(grid) and 0 <= j < len(grid[0])


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                for x,y in direction[grid[i][j]]:
                    row = x + i
                    col = y + j
                    if inbound(row,col):
                        temp = (grid[i][j],(x,y))
                        if grid[row][col] in path[temp]:
                            union((row,col),(i,j))

        initial = find((0,0))
        n ,m = len(grid),len(grid[0])
        final = find((n - 1,m - 1))
        return True if initial == final else False