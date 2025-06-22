# Problem: Toeplitz matrix - https://leetcode.com/problems/toeplitz-matrix/description/

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        m = len(matrix[0])

        for i in range(n):
            j = 0
            temp = matrix[i][j]
            while i< n and j < len(matrix[i]):
                if matrix[i][j] != temp:
                    return False 
                
                i += 1
                j += 1

        for j in range(m):
            i = 0
            temp = matrix[i][j]
            while i < n and j < m:
                if matrix[i][j] != temp:
                    return False 
                
                i += 1
                j += 1

        return True