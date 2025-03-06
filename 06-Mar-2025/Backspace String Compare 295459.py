# Problem: Backspace String Compare - https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        stack1 = []

        for letter in s:

            if stack1 and letter == "#":
                stack1.pop()
            elif letter != "#":
                stack1.append(letter)

        stack2 = []

        for letter in t:

            if stack2 and letter == "#":
                stack2.pop()
            elif letter != "#":
                stack2.append(letter)
        
        print(stack1,stack2)
        return stack2 == stack1
                
            


