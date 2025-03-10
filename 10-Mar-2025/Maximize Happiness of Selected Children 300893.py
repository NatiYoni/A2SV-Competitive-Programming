# Problem: Maximize Happiness of Selected Children - https://leetcode.com/problems/maximize-happiness-of-selected-children/?envType=daily-question&envId=2024-05-09

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:

        happiness.sort(reverse = True)
        

        total = 0
        for i in range(len(happiness)):
            if k > 0:
                total += happiness[i] - i if (happiness[i] - i) > 0 else 0
            else:
                break
            
            k -= 1
            
        
        return total
