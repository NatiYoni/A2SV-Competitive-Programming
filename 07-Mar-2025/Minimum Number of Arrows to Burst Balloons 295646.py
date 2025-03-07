# Problem: Minimum Number of Arrows to Burst Balloons - https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        sort_points = sorted(points, key = lambda x : x[1])
        
        max_ = sort_points[0][1]
        count = 1

        for i in range(1,len(sort_points)):

            if sort_points[i][0] > max_ : # to check if our current arrow  should start. it starts if the previous one stops
                count += 1 # every time we start an arrow we count it 
                max_ = sort_points[i][1]

        return count



