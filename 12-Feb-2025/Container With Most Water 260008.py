# Problem: Container With Most Water - https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0  #left
        r = len(height) - 1 #right
        result = 0 # max area

        while l < r:
            CA = min(height[l],height[r]) * (r - l)
            if CA > result:
                result = CA
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return result
