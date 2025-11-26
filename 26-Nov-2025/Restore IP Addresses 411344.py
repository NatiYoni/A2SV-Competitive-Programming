# Problem: Restore IP Addresses - https://leetcode.com/problems/restore-ip-addresses/

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        n = len(s)
        def bk(i, path):
            if len(path) == 4 and i == n:
                val = ".".join(path)
                # print(val)
                ans.append(val)
                return 
            
            if len(path) > 4:
                return 
            

            for j in range(i,min(i+3,n)):
                val = s[i:j+1]

                if 256 > int(val) >= 0 and str(int(val)) == val:
                    path.append(val)
                    bk(j+1,path)
                    path.pop()
            
          
        
        bk(0,[])
        return ans
        