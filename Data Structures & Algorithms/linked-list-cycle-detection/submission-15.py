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
        loop2 = 0

        print(slow.val, fast.val)

        while True and loop2 < 100:
            # print('***')
            # print(fast != slow)
            while fast != slow and loop < 100:
                # print('!!!!')
                # print(fast.val)
                if fast.next is not None and fast.next.val < fast.val and fast.next.next is not None:
                    # print(1)
                    return True
                if fast.next is not None:
                    # print(2)
                    fast = fast.next
                    continue
                loop += 1
                return False
            

            slow = slow.next
            loop2 += 1