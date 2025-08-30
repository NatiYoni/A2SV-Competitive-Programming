# Problem: Valid Sudoku - https://leetcode.com/problems/valid-sudoku/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        col = [set() for _ in range(n)] 
        row = [set() for _ in range(n)]
        sub = [set() for _ in range(n)]

        for i in range(n):
            for j in range(n):


                val = board[i][j]

                if val == ".":
                    continue
                    
                if val not in col[j]:
                    col[j].add(val)
                else:
                    return False
                
                if val not in row[i]:
                    row[i].add(val)
                else:
                    return False
                

                r = (i // 3) * 3
                c = (j // 3) 

                if val not in sub[r + c ] :
                    sub[r+c].add(val)
                
                else:
                    return False
        
        return True