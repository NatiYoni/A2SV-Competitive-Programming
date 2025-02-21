# Problem: Partition List - https://leetcode.com/problems/partition-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        seeker = head
        holder = head


        temp = head
        flag = False
        while holder and holder.val >= x :
            temp = holder
            holder = holder.next
            flag = True
            


        if flag and temp.next:
            temp.next = temp.next.next
            holder.next = head
            head = holder
        

        while seeker and seeker.next:
            if seeker.val >= x and seeker.next.val < x:
                temp = seeker.next
                seeker.next = seeker.next.next
                temp.next = holder.next
                holder.next = temp
                
                holder = holder.next
            elif seeker.val < x and seeker.next.val < x:
                seeker = seeker.next
                holder = holder.next
            else:
                seeker = seeker.next
                
            
        return head
                



        