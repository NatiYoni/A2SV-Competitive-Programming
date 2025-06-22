# Problem: Split Array Largest Sum - https://leetcode.com/problems/split-array-largest-sum/

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        n = [len(nums)]
        # prefix = [0]
        # for num in nums:
        #     prefix.append(prefix[-1] + num)
        
        def check(mid):
            cnt = 0
            su = 0
            for i in range(n[0]):
                su += nums[i]
                if su > mid:
                    cnt += 1
                    su = nums[i]
                
                
                if cnt > k:
                    return False
            
            if su != 0:
                cnt += 1
            
            return cnt  <= k




        low = 0
        high = sum(nums)
        mx = max(nums)
        while low <= high:
            mid = low + (high - low)//2

            if mid >= mx and check(mid):
                high = mid - 1
                ans = mid
            else:
                low = mid + 1

        return ans


 