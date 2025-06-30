# Problem: Generate Parentheses - https://leetcode.com/problems/generate-parentheses/description/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def bk(open,close,path):
            if len(path) == 2 * n:
                ans.append("".join(path))
                
                return

            if open < n:
                path.append("(")
                bk(open + 1,close, path)
                path.pop()
            
            if close < open:
                path.append(")")
                bk(open, close + 1, path)
                path.pop()
            
        bk(0,0,[])

        return ans    

            





            