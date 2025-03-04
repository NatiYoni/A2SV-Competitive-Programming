# Problem: Minimum Moves to Reach Target Score - https://leetcode.com/problems/minimum-moves-to-reach-target-score/

class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        
        count = 0
        while target > 1:

            if maxDoubles == 0:
                count += target - 1
                target = 0

            elif target % 2 == 1:
                target -= 1
                count += 1
            else:
                target //= 2
                maxDoubles -= 1
                count += 1
            
        return count