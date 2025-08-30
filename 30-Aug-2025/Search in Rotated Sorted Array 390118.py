# Problem: Search in Rotated Sorted Array - https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        h = len(nums) - 1

        while l <= h:
            mid = l + (h-l)//2
            # print(l,h,nums[mid])
            if nums[mid] == target:
                return mid
            
            elif nums[mid] >= nums[l]:
                if nums[l] <= target < nums[mid]:
                    h = mid - 1
                else:
                    l = mid + 1
            
            else:
                if nums[mid] <= target <= nums[h]:
                    l = mid + 1
                else:
                    h = mid - 1
            
        
        return -1

            
