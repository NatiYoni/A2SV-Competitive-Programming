# Problem: Sort List - https://leetcode.com/problems/sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self, left, right):

        dummy = ListNode()
        temp = dummy

        while left and right :
            if left.val <= right.val:
                dummy.next = left
                dummy = dummy.next
                left = left.next
                
            else:
                dummy.next = right
                dummy = dummy.next
                right = right.next
                
        
        while left:
            dummy.next = left
            dummy = dummy.next
            left = left.next
        
        while right:
            dummy.next = right
            dummy = dummy.next
            right = right.next

        
        return temp.next
            
        pass

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        

        if not head or not head.next:
            return head
        

        fast = head.next
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        mid = slow.next
        slow.next = None

        
        left = self.sortList(head)
        right = self.sortList(mid)
        # print(slow.val)

        return self.merge(left, right)

        