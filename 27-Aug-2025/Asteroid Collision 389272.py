# Problem: Asteroid Collision - https://leetcode.com/problems/asteroid-collision/

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        n = len(asteroids)
        stack = []
        for i in range(n):
            val  = asteroids[i]
            sign = val // abs(val)

            while stack and val < 0 and stack[-1] > 0 and abs(val) > stack[-1]:
                stack.pop()
            
            if stack and val < 0 and stack[-1] > 0 and abs(val) == stack[-1]:
                stack.pop()
            
            elif (stack and stack[-1] < 0) or not stack or sign == stack[-1] // abs(stack[-1]):
                stack.append(val)
            
           
        return stack