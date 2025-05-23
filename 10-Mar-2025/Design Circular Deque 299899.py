# Problem: Design Circular Deque - https://leetcode.com/problems/design-circular-deque/

class MyCircularDeque:

    def __init__(self, k: int):
        self.dq = deque()
        self.k = k
      

    def insertFront(self, value: int) -> bool:
        if len(self.dq) < self.k:
            self.dq.appendleft(value)
            return True
               
        return False
    def insertLast(self, value: int) -> bool:
        if len(self.dq) < self.k:
            self.dq.append(value)
            return True 

        return False
            

    def deleteFront(self) -> bool:
        if len(self.dq) > 0:
            self.dq.popleft()
            return True
        
        return False

    def deleteLast(self) -> bool:
        if len(self.dq) > 0:
            self.dq.pop()
            return True
        
        return False

    def getFront(self) -> int:
        return self.dq[0] if self.dq else -1

    def getRear(self) -> int:
        return self.dq[-1] if self.dq else -1

    def isEmpty(self) -> bool:
        return len(self.dq) == 0

    def isFull(self) -> bool:
        return len(self.dq) == self.k
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()