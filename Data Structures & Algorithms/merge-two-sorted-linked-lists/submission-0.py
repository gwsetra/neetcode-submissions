# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        tail = None
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        # print(head)
        # print(list1.val)
        # print(list2.val)
        loop = 0

        while True:
            if list1.val <= list2.val:
                print('if')
                # if head is None:
                #     head = list1
                # head.next = list2
                if list1.next is not None and tail is None:
                    tail = list1.next
                    list1.next = list2
                else:
                    break
                # print(list1.val)
            else:
                print('else')
                # if head is None:
                #     head = list2
                # head.next = list1
                if list2.next is not None and tail is None:
                    tail = list2.next
                    list2.next = list2
                else:
                    break
            
        
            print(tail.val)
            print(tail.next.val)
            print(list1.val)
            print(list1.next.val)
            print(list2.val)
            print(list2.next.val)
            loop +=1
            if loop > 10:
                break
        return tail
        # while head.next is not None:

        
        