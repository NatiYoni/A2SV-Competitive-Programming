# Problem: Find Consecutive Integers from a Data Stream - https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/

class DataStream:

    def __init__(self, value: int, k: int):

        self.value = value
        self.k = k
        self.q = deque()
        self.i = float('-inf')

    def consec(self, num: int) -> bool:

        if len(self.q) < self.k:
            self.q.append(num)
            if num != self.value:
                self.i = len(self.q)
            
            # print(self.i)
            
        else:
            self.q.pop()
            if self.i > 0:
                self.i -= 1

            self.q.append(num)
            if num != self.value:
                self.i = len(self.q)
            # print(self.i)
            
        if self.i <= 0 and len(self.q) == self.k:
            return True
        
        return False
           






# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)