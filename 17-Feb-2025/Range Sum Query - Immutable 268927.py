# Problem: Range Sum Query - Immutable - https://leetcode.com/problems/range-sum-query-immutable/

class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum = [0]
        for num in nums:        
            self.prefix_sum.append(self.prefix_sum[-1] + num)
    def sumRange(self, left: int, right: int) -> int:
            leftSum = self.prefix_sum[left]
            rightSum = self.prefix_sum[right+1]
            return rightSum - leftSum

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
