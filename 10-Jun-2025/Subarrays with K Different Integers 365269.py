# Problem: Subarrays with K Different Integers - https://leetcode.com/problems/subarrays-with-k-different-integers/

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        def atMostK(k):
            ans = 0
            seen = defaultdict(int)
            l = 0
            for i in range(len(nums)):
                seen[nums[i]] += 1

                while len(seen) > k:
                    seen[nums[l]] -= 1

                    if seen[nums[l]] == 0:
                        del seen[nums[l]]

                    l += 1

                ans += i - l + 1
            
            return ans
        
        return atMostK(k) - atMostK(k-1)

