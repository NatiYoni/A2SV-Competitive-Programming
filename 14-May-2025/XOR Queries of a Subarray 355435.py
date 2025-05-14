# Problem: XOR Queries of a Subarray - https://leetcode.com/problems/xor-queries-of-a-subarray/

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        
        xor_arr = []
        temp = 0
        for val in arr:
            temp ^= val
            xor_arr.append(temp)
        
        print(xor_arr)
        ans = []
        for x,y in queries:
            ans.append(xor_arr[y] ^ xor_arr[x-1]) if x > 0 else ans.append(xor_arr[y])
        
        return ans
