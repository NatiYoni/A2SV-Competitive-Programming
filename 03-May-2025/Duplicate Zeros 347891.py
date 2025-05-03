# Problem: Duplicate Zeros - https://leetcode.com/problems/duplicate-zeros/description/?envType=problem-list-v2&envId=two-pointers

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """

        c = arr.count(0)
        
        for i in range(len(arr) - 1, -1, -1):
            if i + c < len(arr):
                arr[i + c] = arr[i]
            if arr[i] == 0:
                c -= 1
                if i + c < len(arr):
                    arr[i + c] = 0



