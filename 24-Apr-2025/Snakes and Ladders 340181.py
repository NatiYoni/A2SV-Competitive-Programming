# Problem: Snakes and Ladders - https://leetcode.com/problems/snakes-and-ladders/

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        

        def inbound(j):
             return  0 <= j < n
             
 
        flag = ((n-1) % 2 == 0) 
        dq = deque()
        dq.append((n-1,0))
        visited = set()
        visited.add((n-1,0))
        roll = 0
        while dq:
            
            # print(dq)
            for i in range(len(dq)):
                
                row,col = dq.popleft()
                
                if (n - 1 - row) % 2 == 0:
                    ans = (n - 1 - row) * n + col + 1

                else:
                    ans = (n - 1 - row) * n + (n - 1 - col) + 1

                if ans == n * n:
                    # print(board)
                    return roll


                for i in range(1,min(7,n*n + 1)):
                    

                    if row >= 0 : 

                        if  (row % 2 == 0) == flag:
                            nc = col + i
                            
                            if inbound(nc):
                                nr = row

                            else:
                                nr = row - 1
                                nc = n - (nc - n) - 1 
                                
                                
                                
                            
                        else:
                            nc = col - i
                            
                            if inbound(nc):
                                nr = row
                            else:
                                nr = row - 1
                                # nc = (nc + n) + 1
                                nc = abs(nc) - 1

                        # if row >= 0 :  
                        if not (0 <= nr < n and inbound(nc)):
                            continue
                        # if 0 <= nr < n and inbound(nc) and ((nr,nc) not in  visited):                            
                        if  board[nr][nc] != -1 :
                            val = board[nr][nc]

                            nr = n - ((val - 1) // n) - 1

                            if (n - 1 - nr) % 2 == 0:
                                nc = (val - 1)  % n

                            else:
                                
                                # nc = val  % n
                                nc = n - 1 - (val - 1) % n
                        
                        if ((nr,nc) not in  visited):
                            dq.append((nr,nc))
                            visited.add((nr,nc))
                                
                                
                            
                        
            # print(roll,dq)
            roll += 1
                    
        
        return -1

        # while dq:
            
        #     # print(dq)
        #     for i in range(len(dq)):
        #         row, col, state = dq.popleft()
        #         # if (row,col) == (0,0):
        #         #     return roll
                    
        #         for i in range(1,min(7,n*n + 1)):

        #                 if state :
        #                     nc = col + i
        #                     if in_bound(nc):
        #                         dq.append((row,nc,state))
        #                         if board[row][nc] != 0:
        #                             board[row][nc] = 0
        #                     else:
        #                         if  0 <= row - 1:
        #                             row -= 1
        #                             if nc - n > 1:
        #                                 nc =  n - (nc - n) - 1 
        #                             if in_bound(nc):
        #                                 dq.append((row  ,nc,not state))
        #                                 if board[row][nc] != 0:
        #                                     board[row][nc] = 0

                        
                        
        #                 else:
        #                     nc = col - i
        #                     if in_bound(nc):
        #                         dq.append((row,nc,state))
        #                         if board[row][nc] != 0:
        #                             board[row][nc] = 0

        #                     else:
        #                         if  0 <= row - 1:
        #                             nc = abs(nc)
        #                             row -= 1
        #                             if in_bound(nc):
        #                                 dq.append((row - 1, nc,not state))
        #                                 if board[row][nc] != 0:
        #                                     board[row][nc] = 0
                            
                            
            
        #     roll += 1
        # print(board)
                        



        