# Problem: The Maximum Number - https://leetcode.com/problems/third-maximum-number/description/

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        f = s = t = float("-inf")

        for num in nums:
            
            if num == f or num == s or num == t:
                continue

            if num > f:
                f, s, t = num, f, s
                
            
            elif num > s:
                s, t = num, s
            
            elif num > t:
                t = num
                
        
        return t if t != float("-inf") else f