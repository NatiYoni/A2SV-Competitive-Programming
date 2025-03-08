# Problem: Broken Calculator - https://leetcode.com/problems/broken-calculator/description/

class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        count = 0

        while target > startValue:

            if target % 2 == 1:
                count += 1
                target += 1

            count += 1
            target //= 2 
        
        return count + startValue - target