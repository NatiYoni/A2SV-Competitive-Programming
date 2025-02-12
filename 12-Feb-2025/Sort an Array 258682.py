# Problem: Sort an Array - https://leetcode.com/problems/sort-an-array/description/

class Solution:
    def heapify(self, arr, n, i):
        largest = i  
        left = 2 * i + 1  
        right = 2 * i + 2  

        if left < n and arr[left] > arr[largest]:
            largest = left

        
        if right < n and arr[right] > arr[largest]:
            largest = right

       
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr, n, largest) 

    def heap_sort(self, arr):
        n = len(arr)
        
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i)

        
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i] 
            self.heapify(arr, i, 0) 

    def sortArray(self, nums: List[int]) -> List[int]:
        self.heap_sort(nums)
        return nums