# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        tail = ListNode(0)
        dummy = tail
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        loop = 0
        # print(head)
        # print(list1.val)
        # print(list2.val)
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                print('list1.val <= list2.val')
                tail.next = list1
                list1 = list1.next
                tail = tail.next
                # tail = list1
                # list1 = list1.next
                # tail.next = list2
            else:
                print('list1.val > list2.val')
                tail.next = list2
                list2 = list2.next
                tail = tail.next
                # tail = list2
                # list2 = list2.next
                # tail.next = list1
            
            print('----**------**---')
            # print(tail.val)
            # print(tail.next.val)
            # print(list1.val)
            # print(list1.next.val)
            # print(list2.val)
            # print(list2.next.val)
        # print(list1.val)
        # print(list2.val)
        if list1 is not None:
            tail.next = list1
 
        if list2 is not None:
            tail.next = list2
            
        return dummy.next


        

        
        