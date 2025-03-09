# Problem: Implement Queue using Stacks - https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:

    def __init__(self):
        self.q = []
        self.i = 0

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        self.i += 1
        return self.q[self.i - 1]

    def peek(self) -> int:
        return self.q[self.i]

    def empty(self) -> bool:
        return len(self.q) == self.i


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()