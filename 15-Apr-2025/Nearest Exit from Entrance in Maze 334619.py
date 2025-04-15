# Problem: Nearest Exit from Entrance in Maze - https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:

        direction = [(1,0),(-1,0),(0,1),(0,-1)]
        def inbound(row,col):
            return 0 <= row < len(maze) and 0 <= col < len(maze[0])

        dq = deque([entrance])
        maze[entrance[0]][entrance[1]] = "+"
        ans = 0 

        while dq:
            ans += 1
            

            for i in range(len(dq)):
                row , col = dq.popleft()
                
                # print(row,col)
                for x,y in direction:
                    nr=x + row
                    nc= y + col

                    if inbound(nr,nc) and maze[nr][nc] == ".":
                        # print(nr,nc,ans)
                        if nr == 0 or nc == 0 or nr == len(maze) -1 or nc == len(maze[0]) - 1:

                            return ans
                        maze[nr][nc] = "+"
                        dq.append([nr,nc])

        
        return -1
                    
                    