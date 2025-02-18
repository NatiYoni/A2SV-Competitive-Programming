# Problem: Interval List Intersections - https://leetcode.com/problems/interval-list-intersections/

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:

        right, left = 0, 0
        result = []
        
        while left < len(firstList) and right < len(secondList):
            start = max(firstList[left][0], secondList[right][0])
            end = min(firstList[left][1], secondList[right][1])
            
            if start <= end:
                result.append([start, end])
            
            if firstList[left][1] < secondList[right][1]:
                left += 1
            else:
                right += 1
        
        return result


             