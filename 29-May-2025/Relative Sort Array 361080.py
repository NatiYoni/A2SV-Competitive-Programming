# Problem: Relative Sort Array - https://leetcode.com/problems/relative-sort-array/description/

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        c = Counter(arr1)
        ans = []
        for val in arr2:
            temp = c[val]
            for j in range(temp):
                ans.append(val)
                c[val] -= 1

        temp = []
        for val in c:
            temp1 = c[val]
            for j in range(temp1):
                temp.append(val)
    
        temp.sort()
        ans.extend(temp)

        return ans
        