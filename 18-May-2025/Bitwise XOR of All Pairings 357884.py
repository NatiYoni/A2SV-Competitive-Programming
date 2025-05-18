# Problem: Bitwise XOR of All Pairings - https://leetcode.com/problems/bitwise-xor-of-all-pairings/description/?envType=problem-list-v2&envId=brainteaser

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:

        ans = 0
        if len(nums1) % 2 == 0 and len(nums2) % 2 == 0:
            return 0
        
  
        if len(nums1) % 2 == 1:
            for val in nums2:
                ans ^= val
       
        # print(ans)
        if len(nums2) % 2 == 1:
            for val in nums1:
                ans ^= val
        
        return ans