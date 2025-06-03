# Problem: Majority Element - https://leetcode.com/problems/majority-element/description/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash = defaultdict(int)

        for val in nums:
            hash[val] += 1

            if hash[val] > len(nums) // 2:
                return val