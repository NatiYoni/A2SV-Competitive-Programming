# Problem: 01 Matrix - https://leetcode.com/problems/01-matrix/

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        dq = deque()
        visited = [[-1]*len(mat[0]) for _ in range(len(mat))]

        print(visited)
        def inBound(row,col):
            if 0 <= row < len(mat) and 0 <= col < len(mat[0]):
                return True
            
            return False

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    dq.append((i,j))
                    visited[i][j] = 0
  
        
        directions = [(0,1), (1,0),(0,-1),(-1,0)]

        while dq:
            for i in range(len(dq)):
                row,col = dq.popleft()
                

                for x,y in directions:
                    nr,nc = row + x, col + y
                    if inBound(nr,nc) and visited[nr][nc] == -1:
                        visited[nr][nc] = 0
                        mat[nr][nc] = mat[row][col] + 1
                        dq.append((nr,nc))
                        
        
        return mat

