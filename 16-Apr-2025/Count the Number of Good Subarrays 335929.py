# Problem: Count the Number of Good Subarrays - https://leetcode.com/problems/count-the-number-of-good-subarrays/description/

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        
        # temp = 0 
        # count = 0
        # d = defaultdict(int)

        # for i,a in enumerate(nums):
        #     d[a] += 1
        #     print(d[a])
        #     if d[a] > 1:
        #         temp += (d[a] * (d[a] - 1)) // 2
        #         print(a,temp)
        #         if len(nums) < k:
        #             return 1
        #         elif temp >= k:
        #             count += 1 
        #             print(count,a,temp)
        # i = 0
        # temp = count
        # while i < len(nums) and temp >= k:
        #     d[nums[i]] -= 1
        #     if d[nums[i]] >= 1 :
        #         count += 1
        #         temp 
            
        #     i += 1

        # return count
        
        ans = 0
        d = defaultdict(int)

        left = 0
        count = 0
        for i in range(len(nums)):
            count += d[nums[i]]
            d[nums[i]] += 1

            while count >= k:
                ans += len(nums) - i
                d[nums[left]] -= 1
                count -= d[nums[left]]
                left += 1

        return ans
