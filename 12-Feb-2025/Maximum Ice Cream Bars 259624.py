# Problem: Maximum Ice Cream Bars - https://leetcode.com/problems/maximum-ice-cream-bars/

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        counts = [0] * (max(costs) + 1)

        for cost in costs:
            counts[cost] += 1
   
        
        maximum_number = 0
        cur_price = 0
        
        for index in range(1,len(counts)):
            cur_price = counts[index] * index

            while counts[index] > 0 and cur_price > coins:
                counts[index] -= 1
                cur_price = counts[index] * index 
                

            

            if cur_price > 0 and cur_price <= coins:
                maximum_number += counts[index]

           

            coins -= cur_price 
        
        return maximum_number