# Problem: Flipping an Image - https://leetcode.com/problems/flipping-an-image/description/

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for arr in image:
            arr.reverse()
            for index, num in enumerate(arr):
                if num == 0:
                    arr[index] = 1
                else:
                    arr[index] = 0

        return image