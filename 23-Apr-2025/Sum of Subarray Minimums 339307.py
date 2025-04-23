# Problem: Sum of Subarray Minimums - https://leetcode.com/problems/sum-of-subarray-minimums/

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        
        stack = []
        ans = 0
        
        # post = 0
        for i in range(len(arr)):
            count = 0
            # post += 1
            
            while stack and arr[i] < stack[-1][0]:
                # print(stack)
                num,pre,post = stack.pop()
     
                # print(len(stack) ,num,i - post)
                ans += num * (1 + pre)  * (i - post) 
                # print(ans)
                count += pre + 1

            # if not stack:
            #     post = 0

            stack.append((arr[i],count,i ))
            

        # print(stack)
        while stack:
            num,pre,post = stack.pop()
            # print(post)

            ans += num * (pre + 1) * (len(arr) - post)

            # ans += (len(stack) - i) * stack[i][0] + (len(stack) - i) * stack[i][0] * stack[i][1]
            # print((len(stack) - i) * stack[i][0] + (len(stack) - i) * stack[i][0] * stack[i][1])

        return ans % (10**9 + 7)
        