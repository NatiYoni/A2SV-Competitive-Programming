# Problem: Selection Sort - https://practice.geeksforgeeks.org/problems/selection-sort/1

class Solution: 
    def selectionSort(self, arr):
        #code here
        for i in range(len(arr)):
            
            smallest = arr[i]
            index = i
            for j in range(i,len(arr)):
                if arr[j] < smallest:
                    index = j
                    smallest = arr[index]
                    
            
            arr[i], arr[index] = arr[index] , arr[i] 
                
                
        
        return arr