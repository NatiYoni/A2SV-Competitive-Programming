# Problem: Stone Game - https://leetcode.com/problems/stone-game/

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)

        dpa = [[0]*n for _ in range(n)] 
        dpb = [[0] *n for _ in range(n)]


        for i in range(n):
            dpa[i][i] = piles[i]
            dpb[i][i] = -piles[i]   
        
        
        for l in range(1,n):
            for i in range(n-1):
                j = l + i

                if j < n:
                    dpa[i][j] = max(dpb[i+1][j] + piles[i], dpb[i][j-1] + piles[j])
                    dpb[i][j] = min(dpa[i+1][j] - piles[i], dpa[i][j-1] - piles[j])
            #
        # print(dpa)

        return dpa[0][-1] > 0
        # dpa = [val for val in piles] 
        # dpb = [-val for val in piles]

        # for l in range(1,n):
        #     tempa = []
        #     tempb = []
        #     for i in range(len(dpa) -1):
        #         j = l + i

        #         tempa.append(max(dpb[i] + piles[j], dpb[i+1] + piles[i]))
        #         tempb.append(min(dpa[i] - piles[j], dpa[i+1] - piles[i]))

        #     dpa = tempa[:]
        #     dpb = tempb[:]
        
        # print(dpa)
        # return dpa[-1] > 0
                
                


        # memo = {}
        # def dp(i,j,turn):
        #     if i > j:
        #         return 0
            
        #     if (i,j,turn) not in memo:
        #         ans = 0
        #         if turn:
        #             ans = max(dp(i+1,j, not turn) + piles[i],dp(i,j-1, not turn) + piles[j])
        #         else:
        #             ans = max(dp(i+1,j, not turn) - piles[i],dp(i,j-1, not turn) - piles[j])
            
        #         memo[(i,j,turn)] = ans
        #     return memo[(i,j,turn)]
    
        # val = dp(0,len(piles) - 1,True)
        # return val > 0
