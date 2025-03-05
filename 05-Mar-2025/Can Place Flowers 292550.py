# Problem: Can Place Flowers - https://leetcode.com/problems/can-place-flowers/

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        count = 1
        total = 0
        for i in range(len(flowerbed)):

            if flowerbed[i] == 0:
                count += 1
            
            else:
                count = 0
            
            print(count)
            if (count >= 3 and count % 2 == 1) or (i == len(flowerbed) - 1 and count >= 2):
                total += 1
        
        
        return total >= n