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
        loop = 0

        print(slow.val, fast.val)

        while True:
            # print('***')
            # print(slow.val, fast.val)
            # print(slow.val, slow.next.val, fast.val, fast.next.val)

            if fast.next == slow:
                return True

            if fast.next is None:
                return False
            
            fast = fast.next
            # # print(slow.val, slow.next.val, fast.val, fast.next.val)
            
            if fast.next == slow:
                return True

            # fast = fast.next
            slow = slow.next
            # loop += 1
            # print(slow.val, slow.next.val, fast.val, fast.next.val)