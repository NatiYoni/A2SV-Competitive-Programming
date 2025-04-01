# Problem: Heaters  - https://leetcode.com/problems/heaters/

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        max_ = 0

        for i in range(len(houses)):

            l = bisect_left(heaters,houses[i])
            print(l)

            if l < len(heaters):

                if l == 0:
                    max_ = max(max_, abs(houses[i] - heaters[l]))
                
                else:
                    
                    max_ = max(max_, min(abs(houses[i] - heaters[l]), abs(houses[i] - heaters[l - 1])))
            else:
                max_ = max(max_, abs(houses[i] - heaters[l - 1]))
            # print(max_)
            
            
        
        return max_



