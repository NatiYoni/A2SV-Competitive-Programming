# Problem: Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return 

        front = end = head

        while end and n > 0:
            end = end.next
            n -= 1

        if not end:
            return head.next
        
        while end.next:
            front = front.next
            end = end.next
        
        if front.next:
            front.next = front.next.next
        else:
            front.next = None
        

        return head