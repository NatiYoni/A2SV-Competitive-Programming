# Problem: Valid Parentheses - https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        myMap = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in myMap:  
                top_element = stack.pop() if stack else ' '
                if myMap[char] != top_element:
                    return False
            else:  
                stack.append(char)
        
        return not stack