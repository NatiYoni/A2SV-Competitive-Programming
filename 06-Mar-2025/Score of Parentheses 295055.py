# Problem: Score of Parentheses - https://leetcode.com/problems/score-of-parentheses/

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        
        stack = []

        
        for p in s:  # p is for parenthsis 

            if p == "(":
                stack.append(0)
    
            else:
                
                if stack[-1] == 0:
                    stack.pop()
                    stack.append(1)
            
                else:
                    val = 0
                    while stack and stack[-1] != 0:
                        val += stack.pop()
                        

                    stack[-1] += 2 * val
        
        return sum(stack)




  