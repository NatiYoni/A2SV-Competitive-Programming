# Problem: Surrounded Regions - https://leetcode.com/problems/surrounded-regions/

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])
        visited = [[0] * m for _ in range(n)]
        
        

        def dfs(row,col):
            if not (0 <= row < n and 0 <= col < m) or board[row][col] == "X" or visited[row][col] == 1:
                return 

            directions = [(-1,0),(0,1),(0,-1),(1,0)]
            # print(row,col)
            # print(board)
            
            temp = board[row][col]
            board[row][col] = "b"
            visited[row][col] = 1
            

            for r,c in directions:
                dfs(row + r,col + c)
                # if row == 2 and col == 3:
                #     print(row + r, col + c)
                #     print(flag)
            
                # if ((row == n -1 or col == m - 1 or row == 0 or col == 0) and temp == "O") or flag:
                #     board[row][col] = "O"
                #     flag = True
                #     return flag


        
        for i in range(n):
            for j in range(m):
                if board[i][j] == "O" and visited[i][j] == 0 and (i == n -1 or j == m - 1 or i== 0 or j == 0):
                    dfs(i,j)
                    # print(i,j)
        # print(board)

        for i in range(n):
            for j in range(m):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "b":
                    board[i][j] = "O"
        