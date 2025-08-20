# Problem: Reverse Linked List - https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
            
        if head.next == None:
            return head

        temp = head
        if head and head.next:
            temp = head.next
            head.next = None

        while temp and temp.next:
            next_temp = temp.next
            temp.next = head
            head = temp
            temp = next_temp
        
        if temp:
            temp.next = head
        
        
        return temp

