# Problem: Longest Increasing Path in a Matrix - https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        def inbound( i, j):
            return 0 <= i < len(matrix) and 0 <= j < len(matrix[0])

        directions = [(-1,0),(0,1),(0,-1),(1,0)]

        visited = [[0]*len(matrix[0]) for _ in range(len(matrix))]
        # max_ = [0]

        memo = {}
        def dfs(row,col):
            res = 0
            visited[row][col] = 1
            for x,y in directions:
                nr = row + x
                nc = col + y
                
                if inbound(nr,nc):

                    if matrix[row][col] < matrix[nr][nc]:
                        if (nr,nc) in memo:
                            res = max(res,memo[(nr,nc)])
                        else:
                            res =  max(res,dfs(nr,nc))

            memo[(row,col)] = res + 1

            return res + 1
        
        ans = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if visited[i][j] == 0:
                    ans = max(ans,dfs(i,j))

        return ans







        # max_ = 0
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):

        #         dq = deque()
        #         dq.append((i,j))
        #         count = 0
        #         while dq:
        #             count += 1
        #             for _ in range(len(dq)):
        #                 row,col = dq.popleft()

        #                 for x,y in directions:
                            
        #                     nr,nc = row + x, col + y
                            
        #                     if inbound(nr,nc) and matrix[row][col] < matrix[nr][nc]:
        #                         # print(nr,nc)
        #                         dq.append((nr,nc))

        #         max_ = max(max_,count)
        
        # return max_
        