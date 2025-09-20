# Problem: Find Indices With Index and Value Difference I - https://leetcode.com/problems/find-indices-with-index-and-value-difference-i/description/

class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        n = len(nums)

        ans = []
        for idx , val in enumerate(nums):
            if idx + indexDifference < n:
                newIdx = idx + indexDifference
                for j in range(newIdx, n):
                    if abs(nums[idx] - nums[j]) >= valueDifference:
                        return [idx,j]
            else:
                break
        return [-1,-1]