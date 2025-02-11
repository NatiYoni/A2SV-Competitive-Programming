# Problem: How Many Numbers Are Smaller Than the Current Number - https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp = sorted(nums)
        result = [0] * len(nums)
        count = 0
        _map_ = {}

        for index,num in enumerate(temp):
            if num not in _map_:
                _map_[num] = count

            count += 1

        for index, num in enumerate(nums):
            result[index]= _map_[num]


        return result

