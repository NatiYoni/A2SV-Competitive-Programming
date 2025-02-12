# Problem: Pancake Sorting - https://leetcode.com/problems/pancake-sorting/

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:

        def reverse(end):

            start = 0
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1

        length = len(arr)
        output = []
        for i in range(length - 1,-1,-1):
            max_ = i
            for j in range(i, -1, -1):
                if arr[j] > arr[max_]:
                    max_ = j
            if i != max_:
                reverse(max_)
                reverse(i)
                output.append(max_ + 1)
                output.append(i + 1)
        return output 

            



            