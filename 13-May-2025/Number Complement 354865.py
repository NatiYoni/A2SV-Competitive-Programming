# Problem: Number Complement - https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:
        stack = []
        while num > 0:
            stack.append(num % 2)
            num //= 2
        
        for i,val in enumerate(stack):
            if val == 0:
                stack[i] = str(1)
            else:
                stack[i] = str(0)
        
        stack.reverse()

        
        return int("0b"+"".join(stack),2)


