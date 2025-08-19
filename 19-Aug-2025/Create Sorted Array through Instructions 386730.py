# Problem: Create Sorted Array through Instructions - https://leetcode.com/problems/create-sorted-array-through-instructions/

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        Mod = 10**9 + 7

        if len(instructions) <= 2:
            return 0
        

        
        for i in range(len(instructions)):
            instructions[i] = (instructions[i],i)

        less = [0] * len(instructions)
        great = [0] * len(instructions)

        def conqure(left,right):
            for val in right:
                less[val[1]] += bisect_left(left, (val[0], -float('inf')))
                great[val[1]] += len(left) - bisect_right(left, (val[0], float('inf')))
                    


            i = 0
            j = 0
            new_arr = []
            while i < len(left) and j < len(right):
                if left[i][0] <= right[j][0]: 
                    new_arr.append(left[i])
                    i += 1
                else:
                    new_arr.append(right[j])
                    j += 1
            
            new_arr.extend(left[i:])
            new_arr.extend(right[j:])
            return new_arr




        def divide(l, r):
            if r - l <= 1:
                return instructions[l:r] 

            mid = l + (r - l)//2
            left = divide(l,mid)
            right = divide(mid,r)
            return conqure(left,right)

        divide(0,len(instructions))
        
        ans = 0
        for i in range(len(instructions)):
            ans += min(great[i],less[i])
        return ans % Mod
        
        
        