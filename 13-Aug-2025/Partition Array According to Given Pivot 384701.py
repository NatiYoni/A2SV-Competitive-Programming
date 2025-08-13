# Problem: Partition Array According to Given Pivot - https://leetcode.com/problems/partition-array-according-to-given-pivot/description/

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = [val for val in nums if val < pivot]
        great = [val for val in nums if val > pivot]

        cur  = len(nums) - (len(less) + len(great))
        
        return less + [pivot] * cur + great