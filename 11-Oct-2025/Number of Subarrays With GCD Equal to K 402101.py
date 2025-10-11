# Problem: Number of Subarrays With GCD Equal to K - https://leetcode.com/problems/number-of-subarrays-with-gcd-equal-to-k/description/

class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        l = 0
        ans = 0
        for i in range(len(nums)):
            cur = 0
            for j in range(i,len(nums)):
                cur = gcd(cur,nums[j])

                if cur == k:
                    ans += 1
        return ans