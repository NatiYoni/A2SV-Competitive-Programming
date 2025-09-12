# Problem: Sum of Even Numbers After Queries - https://leetcode.com/problems/sum-of-even-numbers-after-queries/description/

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans = 0
        for num in nums:
            if num % 2 == 0:
                ans += num
        
        out = []
        for val, idx in queries:
            if nums[idx] % 2 == 1:
                if val % 2 == 1:
                    ans += val + nums[idx]
                
                nums[idx] += val
            else:
                if val % 2 == 0:
                    ans += val
                else:
                    ans -= nums[idx]
                
                nums[idx] += val
            
            out.append(ans)
        
        return out