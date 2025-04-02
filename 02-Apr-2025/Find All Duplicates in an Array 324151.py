# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        output = []
        temp = set()

        for i in nums:
            if i in temp:
                output.append(i)
                continue
            temp.add(i)
            
        return output