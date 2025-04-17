# Problem: Flood Fill - https://leetcode.com/problems/flood-fill/

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        dq = deque([[sr,sc]])
        or_color = image[sr][sc]

        direction = [(1,0),(-1,0),(0,1),(0,-1)]
        visited = [[0]*len(image[0]) for _ in range(len(image))]

        def inbound(row,col):
            return 0 <= row < len(image) and 0 <= col < len(image[0])


        while dq:
            for _ in range(len(dq)):
                row,col = dq.popleft()

                for x, y in direction:
                    nr, nc = row + x, col + y
                    if inbound(nr,nc) and image[nr][nc] == or_color and visited[nr][nc] == 0:
                        visited[nr][nc] = -1
                        image[nr][nc] = color
                        dq.append((nr,nc))
        
        image[sr][sc] = color
        return image