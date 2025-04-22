# Problem: Design browser history  - https://leetcode.com/problems/design-browser-history/

class ListNode:
    def __init__(self, val=0, next=None,pre=None):
        self.val = val
        self.next = next
        self.pre = pre

class BrowserHistory:

    def __init__(self, homepage: str):
        self.cur =  ListNode(homepage)
        
        
    def visit(self, url: str) -> None:
        new_node = ListNode(url)
        self.cur.next = new_node
        new_node.pre = self.cur

        self.cur = new_node
        # print(self.cur.val)
        # return self.cur.val

    def back(self, steps: int) -> str:
        while steps > 0 and self.cur.pre:
            self.cur = self.cur.pre
            steps -= 1
        
        return self.cur.val


    def forward(self, steps: int) -> str:
        while steps > 0 and self.cur.next:
            self.cur = self.cur.next
            steps -= 1
        
        return self.cur.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)