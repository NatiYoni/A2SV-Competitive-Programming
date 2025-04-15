# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        direction = [(1,0),(-1,0),(0,1),(0,-1)]

        dq = deque()
        temp = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    dq.append((i,j))
        def inbound(row,col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
        # print(dq)
        count = 0
        while dq: 
            count += 1
            for i in range(len(dq)):
                x, y = dq.popleft()

                for a, b in direction:
                    nx, ny = x + a,y + b
                    if inbound(nx,ny) and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        dq.append((nx,ny))
        
        # print(grid)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        
        return count - 1 if count > 0 else 0
