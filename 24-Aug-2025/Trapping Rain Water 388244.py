# Problem: Trapping Rain Water - https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, height: List[int]) -> int:

        n = len(height)
        stack = []
        ans = 0
        for i in range(n):
            temp = 0
            while stack and stack[-1][0] <= height[i]:
                val = stack.pop()
                ans += (min(val[0] ,height[i])- temp) * (i - val[1] - 1)
                temp = val[0]

                if stack and stack[-1][0] > height[i] and temp < height[i]:
                    ans += (min(stack[-1][0] ,height[i])- temp) * (i - stack[-1][1] - 1)
                # print(stack,ans)
            stack.append((height[i],i,temp))
        
            # print(stack)
        return ans
