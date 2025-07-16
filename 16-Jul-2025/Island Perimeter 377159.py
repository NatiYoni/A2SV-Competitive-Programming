# Problem: Island Perimeter - https://leetcode.com/problems/island-perimeter/description/

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def in_bound(x,y):
            return 0 <= x < len(grid) and 0<= y < len(grid[0])

        direction = [(0,1),(1,0),(0,-1),(-1,0)]

        n = len(grid)
        m = len(grid[0])

        visited = [[0] *m for _ in range(n)]
        dq = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    dq.append((i,j))
                    visited[i][j] = 1
        
        ans = 0
        while dq:
            row,col = dq.popleft()
            
            for i,j in direction:
                nr = row + i
                nc = col + j

                if in_bound(nr,nc):
                    if grid[nr][nc] == 1:
                        if visited[nr][nc] == 0:
                            dq.append((nr,nc))
                            visited[nr][nc] = 1
                    else:
                        ans += 1
                else:
                    ans += 1
                    
        return ans


