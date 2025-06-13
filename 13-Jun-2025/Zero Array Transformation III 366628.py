# Problem: Zero Array Transformation III - https://leetcode.com/problems/zero-array-transformation-iii/description/

class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        queries.sort()
        heap = []
        operation = 0
        diff = [0] * (len(nums) + 1)

        r = 0
        for l,val in enumerate(nums):
            operation += diff[l]

            while r < len(queries) and queries[r][0] == l:
                heappush(heap, -queries[r][1])
                r += 1
            
            while operation < val and heap and -heap[0] >= l:
                operation += 1
                diff[-heappop(heap) + 1] -= 1
            if operation < val:
                return -1

            # print(diff)
        return len(heap)

    