# Problem: Number of Recent Calls - https://leetcode.com/problems/number-of-recent-calls/

class RecentCounter:

    def __init__(self):

        # self.counter = 0     
        self.q =  deque()   

    def ping(self, t: int) -> int:

        if not self.q:
            self.q.append(t)

        elif t - self.q[0] > 3000:
            # print(t - self.q[0])
            while self.q and  t - self.q[0] > 3000:
                self.q.popleft()
            self.q.append(t)

        else:
            self.q.append(t)


        return len(self.q)


        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)