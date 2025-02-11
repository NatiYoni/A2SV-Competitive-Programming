# Problem: H-Index - https://leetcode.com/problems/h-index/

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        length = len(citations)
        max_num = 0
        result = [0] * length

        for index, num in enumerate(citations):
            result[index] = min(num, length - index)

        return max(result) 
            
            