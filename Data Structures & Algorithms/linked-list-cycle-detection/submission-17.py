# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # using fast slow
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False

        fast = head.next
        slow = head

        # print(slow.val, fast.val)

        while fast != slow:
            if fast.next is None or fast.next.next is None:
                return False
            
            fast = fast.next.next
            slow = slow.next
        
        return True
