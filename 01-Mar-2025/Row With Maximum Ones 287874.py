# Problem: Row With Maximum Ones - https://leetcode.com/problems/row-with-maximum-ones/

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        ans = 0
        index = 0
        for i in range(len(mat)):
            temp = sum(mat[i])

            if temp > ans:
                ans = temp
                index = i
        
        return [index, ans] 
