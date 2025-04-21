# Problem: Minesweeper - https://leetcode.com/problems/minesweeper/

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        x,y = click
        if board[x][y] == "M":

            board[x][y] = "X"
            return board


            
        direction = [(-1,0),(0,1),(0,-1),(1,0),(1,1),(-1,-1),(-1,1),(1,-1)]

        def inbound(grid, i, j):
            return 0 <= i < len(grid) and 0 <= j < len(grid[0])

        dq = deque()
        dq.append((x,y))
        
        visited = [[0 for _ in range(len(board[0]))] for i in range(len(board))]

        while dq:
            row,col = dq.popleft()
            count = 0
            neigh = []

            for x, y in direction:
                nr = row + x
                nc = col + y
                
                if inbound(board,nr,nc):
                    if board[nr][nc] == "E":
                        neigh.append((nr,nc))
                    elif board[nr][nc] == "M":
                        count += 1
            
            if count > 0:
                board[row][col] = str(count)

            else:
                board[row][col] = "B"

                for a, b in neigh:
                    if visited[a][b] == 0:
                        visited[a][b] = 1
                        dq.append((a,b))

        return board