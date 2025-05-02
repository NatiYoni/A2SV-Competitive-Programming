# Problem: Merge k Sorted Lists - https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        arr = []
        for l in lists:
            while l:
                heappush(arr,l.val)
                l = l.next
        
        dummy = ListNode(0)
        temp = dummy
        while arr:
            temp.next = ListNode(heappop(arr))
            temp = temp.next
            
        # print(arr)
        return dummy.next