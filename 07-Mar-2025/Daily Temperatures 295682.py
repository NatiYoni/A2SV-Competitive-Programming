# Problem: Daily Temperatures - https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        ans = [0] * len(temperatures)

        for i, t in enumerate(temperatures):

            while stack and t > stack[-1][0]:

                d = stack[-1][1] # the differece between the days
                stack.pop()
                ans[d] = i - d
                # print(i - d, d)
                d += 1

            stack.append((t,i))
            # print(stack)
        return ans
