# Problem: Heaters - https://leetcode.com/problems/heaters/

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        # heaters.sort()
        # ans = 0

        # for i in range(len(houses)):

        #     l = bisect_right(heaters,houses[i])

        #     prev = houses[i] - heaters[l-1] if l-1 >= 0 else float('inf')

        #     next = heaters[l] - houses[i] if l < len(heaters) else float('inf')

        #     res = min(prev,next)
        #     ans = max(ans,res)
        
        # return ans

        # The above code works 


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



