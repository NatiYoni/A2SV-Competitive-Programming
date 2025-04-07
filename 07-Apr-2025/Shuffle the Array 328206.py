# Problem: Shuffle the Array - https://leetcode.com/problems/shuffle-the-array/

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        l = 0
        r = n

        ans = []
        while l < n:
            ans.append(nums[l])
            ans.append(nums[r])
            l += 1
            r += 1
        return ans
