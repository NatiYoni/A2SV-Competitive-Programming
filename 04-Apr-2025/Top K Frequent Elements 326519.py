# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
            c = Counter(nums)

            sorted_c = sorted(c.items(), key = lambda x :  x[1], reverse = True)
            
            ans = []
            for i in range(k):
                ans.append(sorted_c[i][0])
            
            return ans



        
        