# Problem: Clear Digits - https://leetcode.com/problems/clear-digits/description/

class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []

        for l in s:
            stack.append(l)

            if stack and stack[-1].isdigit():
                stack.pop()

                if stack:
                    stack.pop()
        
        return "".join(stack)