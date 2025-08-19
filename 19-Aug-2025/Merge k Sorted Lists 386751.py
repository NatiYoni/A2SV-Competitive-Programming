# Problem: Merge k Sorted Lists - https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        for root in lists:
            while root:
                heappush(heap,root.val)
                root = root.next
        
        dummy = ListNode()
        temp = dummy
        while heap:
            temp.next = ListNode(heappop(heap))
            temp = temp.next
        
        return dummy.next
