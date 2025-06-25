# Problem: K Closest Points to Origin - https://leetcode.com/problems/k-closest-points-to-origin/

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        for i in range(len(points)):
            temp = sqrt(points[i][0] ** 2 + points[i][1] ** 2)
            res.append((temp,i))
        
        res.sort()
        return [points[res[i][1]] for i in range(k)]
