# Problem: Convert 1D Array Into 2D Array - https://leetcode.com/problems/convert-1d-array-into-2d-array/

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        ans = [[] for _ in range(m)] 
        # print(ans)

        count = 0
        index = 0
        for i in range(len(original)):
            if count == n:
                count = 0
                index += 1

            if index >= m:
                return []

            ans[index].append(original[i])

            count += 1
        
        return ans if len(ans[-1]) == n else []


