# Problem: Tuple with Same Product - http://leetcode.com/problems/tuple-with-same-product

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        my_dict = {}
        ans = 0

        for i in range(len(nums)):
            for j in range(i+1,len(nums)): 
                multiple =nums[i] * nums[j]

                if multiple not in my_dict:
                    my_dict[multiple] = 1
                    continue

                my_dict[multiple] += 1

        for val in my_dict.values():
            if val > 1:
                ans += val * (val - 1) * 4
        
        return ans
         