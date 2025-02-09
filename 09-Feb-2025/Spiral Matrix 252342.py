# Problem: Spiral Matrix - https://leetcode.com/problems/spiral-matrix/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        output = []
        top, bottom = 0, len(matrix) 
        left, right = 0, len(matrix[0]) 

        while top < bottom and left < right:

            for i in range(left,right): #left to right
                output.append(matrix[top][i])
            
            top += 1

            for i in range(top,bottom): #top to down
                output.append(matrix[i][right-1])
            
            right -= 1
            if top < bottom:
                for i in range(right-1, left - 1, -1): #right to left
                    output.append(matrix[bottom-1][i])
            
            bottom -= 1

            if left < right:
                for i in range(bottom - 1, top - 1, -1): #bottom to top
                    output.append(matrix[i][left])

            left += 1

        return output
                