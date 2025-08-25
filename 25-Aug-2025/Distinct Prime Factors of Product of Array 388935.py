# Problem: Distinct Prime Factors of Product of Array - https://leetcode.com/problems/distinct-prime-factors-of-product-of-array/

class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        seen = set()

        for num in nums:
            i = 2

            while i <= num // i:
                if num % i == 0:
                    seen.add(i)

                    while num % i == 0:
                        num //= i
            
                i += 1
            if num > 1:
                seen.add(num)
        
        return len(seen)