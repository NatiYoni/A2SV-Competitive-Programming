# Problem: Evaluate Reverse Polish Notation - https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        operations = {"+","-","*","/"}

        stack = []
        for token in tokens:

            if token in operations:
                val1 = stack.pop()
                val2 = stack.pop()
                
                if token == "+":
                    stack.append(int(val1) + int(val2))
                elif token == "-":
                    stack.append(int(val2) - int(val1))
                elif token == "*":
                    stack.append(int(val1) * int(val2))
                else:
                    stack.append(int(val2) / int(val1))
                
            else:
                stack.append(token)
        
        return int(stack[-1])


