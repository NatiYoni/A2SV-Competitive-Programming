# Problem: Check If Array Pairs Are Divisible by k - https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        n = len(arr)
        cnt = [0] * k
        
        for val in arr:
            cnt[val%k] += 1
        #     print(val, val%k)
        # print(cnt)
        if cnt[k//2]  % 2  and k % 2 == 0:
            return False
        
             
        for i in range(1,k):
            if cnt[k-i] != cnt[i]:
                return False
        
        return True

