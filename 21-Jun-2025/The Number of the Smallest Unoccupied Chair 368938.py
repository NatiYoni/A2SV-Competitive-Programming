# Problem: The Number of the Smallest Unoccupied Chair - https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair/description/

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        
        arrival_leave = [] 
        for i in range(len(times)):
            s,e = times[i]
            arrival_leave.append((s,1,i))
            arrival_leave.append((e,0,i))
        
        arrival_leave.sort()

        nums = [i for i in range(len(times))]
        heapify(nums)

        seatHolders = defaultdict(int)

        for val,s_t,index in arrival_leave:
            if s_t == 0:
                heappush(nums,seatHolders[index])
            else:
                ans = heappop(nums)
                seatHolders[index] = ans
                if targetFriend == index:
                    return ans
                
        # print(seatHolders)
        return seatHolders[targetFriend]