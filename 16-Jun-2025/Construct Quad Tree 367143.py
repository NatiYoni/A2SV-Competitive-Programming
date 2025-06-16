# Problem: Construct Quad Tree - https://leetcode.com/problems/construct-quad-tree/description/

"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

       
        def divide(n, r, c):
            oneLove = True
            for i in range(n):
                for j in range(n):
                    if grid[r][c] != grid[r + i][c + j]:
                        oneLove = False
                        break
            
            if oneLove:
                return Node(grid[r][c], True)

            n = n // 2
            topleft = divide(n,r,c)
            bottomleft = divide(n,r + n,c)
            topright = divide(n,r ,c +  n)
            bottomright = divide(n,r + n ,c + n)

            return Node(0,False, topleft,topright,bottomleft,bottomright)

        return divide(len(grid),0,0)
