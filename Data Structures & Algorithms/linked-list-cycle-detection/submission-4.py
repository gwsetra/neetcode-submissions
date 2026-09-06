# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        cur = head

        if head == []:
            return False

        while True:
            print(cur.val, cur.next)

            if cur.next is None:
                return False
            
            if cur.val in visited:
                return True
            
            visited.add(cur.val)

            cur = cur.next
