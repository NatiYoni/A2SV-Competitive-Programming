# Problem: Furthest Building You Can Reach - https://leetcode.com/problems/furthest-building-you-can-reach/

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        prefix = []
        for i in range(1,len(heights)):
            prefix.append(heights[i] - heights[i-1])
        
        ans = 0
        res = []
        sum_ = 0
        print(prefix)

        for val in prefix:
            
            if val > 0:
                
                heappush(res,-val)
                sum_ += val
                # print(sum_,res)
                if sum_ + res[0] > bricks and ladders > 0:
                    
                    temp = heappop(res)
                    sum_ -=  abs(temp)
                    ladders -= 1

                    if sum_ > bricks and ladders == 0:
                        break
                
                elif sum_  > bricks and ladders == 0:
                    break
                
            ans += 1
        
        return ans 


                
