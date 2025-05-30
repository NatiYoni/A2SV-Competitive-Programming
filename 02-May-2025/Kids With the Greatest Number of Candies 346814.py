# Problem: Kids With the Greatest Number of Candies - https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_ = max(candies)

        ans = [False for _ in range(len(candies))]

        for i,candie in enumerate(candies):
            if candie + extraCandies >= max_:
                ans[i] = True
        
        return ans