# Problem: Excel Sheet Column Title - https://leetcode.com/problems/excel-sheet-column-title/description/?envType=problem-list-v2&envId=string

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:

        result = []
        
        while columnNumber > 0:
            columnNumber -= 1  
            remainder = columnNumber % 26
            result.append(chr(remainder + ord('A')))
            columnNumber //= 26 
        
        return ''.join(result[::-1])
            
        

            
