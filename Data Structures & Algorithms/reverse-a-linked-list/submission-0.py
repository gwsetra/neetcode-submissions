# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        if head is None or head.next is None:
            return head
        elif head.next.next is None:
            head = head.next
            head.next = curr
            curr.next = None
            return head
        else:
            new_head = self.reverseList(head.next)
            head.next.next = head   # flip the link
            head.next = None        # cut the old link

            return new_head

