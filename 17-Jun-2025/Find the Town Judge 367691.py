# Problem: Find the Town Judge - https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        town = defaultdict(int)
        
        for out, inc in trust:
            town[inc] += 1
            town[out] -= 1
        
        # print(town)
        for i in range(1,n + 1):
            if town[i] == n - 1:
                return i
        
        return -1