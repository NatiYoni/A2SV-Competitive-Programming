# Problem: Check if All the Integers in a Range Are Covered - https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/description/

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        arr = [0] * 52

        for st, end in ranges:
            arr[st] += 1
            arr[end+1] -= 1
        
        for i in range(1, len(arr)):
            arr[i] += arr[i-1]

        for i in range(left, right + 1):
            if arr[i] == 0:
                return False
        
        return True