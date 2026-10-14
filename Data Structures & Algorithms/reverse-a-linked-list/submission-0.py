# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr: #while curr is not at the end of the linked list
            nxt = curr.next #save the rest of the list
            curr.next = prev # reverse the pointer, make curr point at the last val
            prev = curr # move prev forward
            curr = nxt #move curr forward

        return prev
         



