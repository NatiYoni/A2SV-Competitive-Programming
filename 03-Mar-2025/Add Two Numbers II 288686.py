# Problem: Add Two Numbers II - https://leetcode.com/problems/add-two-numbers-ii/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        arr1, arr2 = [], []

        cur1 = l1
        while cur1:
            arr1.append(cur1.val)
            cur1 = cur1.next
        
        cur2 = l2
        while cur2:
            arr2.append(cur2.val)
            cur2 = cur2.next
        
        carry = 0
        head = None
        
        while arr1 or arr2 or carry:

            val1 = arr1.pop() if arr1 else 0
            val2 = arr2.pop() if arr2 else 0

            temp = val2 + val1 + carry
            carry = temp // 10 
            new_node = ListNode(temp % 10)
            new_node.next = head
            head = new_node
        
        return head
