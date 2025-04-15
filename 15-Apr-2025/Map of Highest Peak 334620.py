# Problem: Map of Highest Peak - https://leetcode.com/problems/map-of-highest-peak/description/

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:

        direction = [(1,0),(-1,0),(0,1),(0,-1)]

        def inbound(row,col):
            return 0 <= row < len(isWater) and 0 <= col < len(isWater[0])

        
        dq = deque()
        for i in range(len(isWater)):
            for j in range(len(isWater[0])):
                if isWater[i][j] == 1:
                    dq.append([i,j])
                    isWater[i][j] = 0
                else:
                
                    isWater[i][j] = -1

        # print(isWater)

        while dq:
            for i in range(len(dq)):

                row, col = dq.popleft()

                for x, y in direction:
                    nr,nc = x + row, y + col

                    if inbound(nr,nc) and isWater[nr][nc] == -1:
                        isWater[nr][nc] = isWater[row][col] + 1
                    
                        dq.append([nr,nc])

        return isWater