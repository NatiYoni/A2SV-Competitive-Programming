# Problem: Diagonal Traverse - https://leetcode.com/problems/diagonal-traverse/

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        output = []
        up_direction = True
        rows = len(mat)
        cols = len(mat[0])
         
        row, col = 0, 0 
        for i in range(rows):
            for j in range(cols):
                output.append(mat[row][col])

                if up_direction:
                    if col == cols - 1:
                        row += 1
                        up_direction = False
                    elif row == 0:
                        col += 1
                        up_direction = False
                    else:
                        row -= 1
                        col += 1
                else:
                    if row == rows - 1:
                        col += 1
                        up_direction = True
                    elif col == 0:
                        row += 1
                        up_direction = True
                    else:
                        col -= 1
                        row += 1
        return output


