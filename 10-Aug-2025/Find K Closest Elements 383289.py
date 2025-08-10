# Problem: Find K Closest Elements - https://leetcode.com/problems/find-k-closest-elements/

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        idx = bisect_right(arr, x) - 1
        l = idx
        r = idx + 1 
        
        n = len(arr)
        ans = []
        while (l >= 0 or r < n) and len(ans) < k :
            if l >= 0 and r < n:
                if abs(arr[l] - x) <= abs(arr[r] - x):
                    ans.append(arr[l])
                    l -= 1
                else:
                    ans.append(arr[r])
                    r += 1

            elif l >= 0:
                ans.append(arr[l])
                l -= 1

            elif r < n:
                ans.append(arr[r])
                r += 1
            
            else:
                break
            
            
            
        
        return sorted(ans)
