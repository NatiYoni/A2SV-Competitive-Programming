# Problem: Design Linked List - https://leetcode.com/problems/design-linked-list/

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        
        if index >= self.size:
            return -1
        
        temp = self.head
        for _ in range(index):
            temp = temp.next
        
        return temp.value

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)        
        new_node.next = self.head
        self.head = new_node
        
        if self.size == 0:  
            self.tail = new_node

        self.size += 1

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)

        if self.size == 0: 
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:

        if index > self.size:
            return

        
        if index == 0:
            self.addAtHead(val)
            return
        if index == self.size:
            self.addAtTail(val)
            return

        new_node = Node(val)
        temp = self.head

        for _ in range(index - 1):
            temp = temp.next

        new_node.next = temp.next
        temp.next = new_node
        self.size += 1
         

    def deleteAtIndex(self, index: int) -> None:

        if index >= self.size:
            return  

        if index == 0: 
            self.head = self.head.next
            if self.size == 1:  
                self.tail = None
            self.size -= 1
            return

        temp = self.head
        for _ in range(index - 1):
            temp = temp.next

        temp.next = temp.next.next 

        if index == self.size - 1:  
            self.tail = temp

        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)