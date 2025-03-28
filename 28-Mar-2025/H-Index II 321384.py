# Problem: H-Index II - https://leetcode.com/problems/h-index-ii/description/

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)

        def check(mid):
            if citations[mid] >= n - mid:
                return True
            else:
                return False
            pass
        
        l = 0
        h = len(citations) - 1
        
        while l <= h:
            m = l + (h - l)//2
            
            if check(m):
                h = m - 1
            
            else:
                l = m + 1
        
        return n - l
