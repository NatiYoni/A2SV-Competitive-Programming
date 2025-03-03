# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        stack = []

        while head:

            stack.append(head.val)
            head = head.next

        max_ = 0
        left , right = 0, len(stack) - 1

        while left < right:
            max_ = max(max_, stack[right] + stack[left])
            left += 1
            right -= 1
        
        return max_

