# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        l, h = 0, len(matrix) * len(matrix[0]) - 1 

        while l <= h:
            mid = (l + h) // 2

            if  matrix[mid // len(matrix[0])][ mid % len(matrix[0])] == target:
                return True

            elif matrix[mid // len(matrix[0])][ mid % len(matrix[0])] > target:
                h = mid - 1

            else:
                l = mid + 1
    
        return False