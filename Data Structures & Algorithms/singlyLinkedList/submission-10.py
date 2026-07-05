class Node():
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head  = Node(None)
        self.tail = Node(None)
        self.lastelem = None
        self.length = 0
    
    def get(self, index: int) -> int:
        print('inside get finding index', index)
        if self.head.next is None or index > self.length:
            return -1
        curr = self.head.next
        loop = 0
        while curr.next is not None and loop != index:
            # print(curr.val, curr.next)
            curr = curr.next
            loop += 1
        print(-1 if loop < index else curr.val)
        return -1 if loop < index else curr.val

    def insertHead(self, val: int) -> None:
        print('insertHead', val)
        nnode = Node(val)

        if self.head.next is None:
            # print('self.head.next is None')
            nnode.next = self.tail
            self.head.next = nnode
            self.lastelem = nnode
            # self.get(4)
        else:
            # print('self.head.next is not None')
            nnode.next = self.head.next
            self.head.next = nnode
            # self.get(4)
        self.length += 1

    def insertTail(self, val: int) -> None:
        print('insertTail', val)
        nnode = Node(val)

        if self.head.next is None :
            nnode.next = self.tail
            self.head.next = nnode
            self.lastelem = nnode
        else:
            # print('insertTail element exists')
            # print(self.lastelem.next)
            nnode.next = self.tail
            self.lastelem.next = nnode
            # self.get(4)
        self.length += 1

    def remove(self, index: int) -> bool:
        print('remove index', index)
        curr = self.head
        counter = -1
        print(index, self.length)

        if index >= self.length or self.length == 0:
            return False


        while counter != index-1:
            curr = curr.next
            counter += 1
        
        curr.next = curr.next.next
        self.length -= 1

        return True
        


    def getValues(self) -> List[int]:
        result = []
        curr = self.head.next
        loop = 0
        if self.length == 0:
            return result
        while curr.next is not None:
            print(curr.val, curr.next)
            result.append(curr.val)
            curr = curr.next
            loop += 1

        return result
