# Problem: Left-and-right-sum-differences - https://leetcode.com/problems/left-and-right-sum-differences/

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left = [0]
        right = [0]
        n = len(nums)

        for i in range(n - 1):
            left.append(left[-1] + nums[i])
            right.append(right[-1] + nums[n - i - 1])
        
        right.reverse()

        ans = [0] * len(left)
        for i in range(len(right)):
            ans[i] = abs(left[i] - right[i])
        
        return ans



        
        
            