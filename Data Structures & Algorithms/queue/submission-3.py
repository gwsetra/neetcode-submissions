class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class Deque:
    
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.length = 0

    def isEmpty(self) -> bool:
        return self.length == 0

    def append(self, value: int) -> None:
        print('inside append', value)
        nnode = Node(value)

        if self.length == 0:
            self.head.next = nnode
            self.tail.prev = nnode
            nnode.prev = self.head
            nnode.next = self.tail
        else:
            self.tail.prev.next = nnode
            nnode.prev = self.tail.prev
            self.tail.prev = nnode
            nnode.next = self.tail
        self.length += 1
        self.printall()
            

    def appendleft(self, value: int) -> None:
        print('inside appendleft', value)
        nnode = Node(value)

        if self.length == 0:
            self.head.next = nnode
            self.tail.prev = nnode
            nnode.prev = self.head
            nnode.next = self.tail
        else:
            nnode.next = self.head.next
            nnode.prev = self.head
            self.head.next.prev = nnode
            self.head.next = nnode
        self.length += 1
        self.printall()

    def pop(self) -> int:
        print('inside pop')
        if self.length == 0:
            return -1

        if self.length == 1:
            tmp = self.head.next
            self.head.next = self.tail
            self.tail.prev = self.head
            tmp.prev = None
            tmp.next = None
        else:
            tmp = self.tail.prev
            self.tail.prev.prev.next = self.tail
            self.tail.prev = self.tail.prev.prev
        self.length -= 1
        self.printall()
        return tmp.val


    def popleft(self) -> int:
        print('inside popleft')
        if self.length == 0:
            return -1
            
        if self.length == 1:
            tmp = self.head.next
            self.head.next = self.tail
            self.tail.prev = self.head
            tmp.prev = None
            tmp.next = None
        else:
            tmp = self.head.next
            self.head.next.next.prev = self.head
            self.head.next = self.head.next.next

        self.length -= 1
        self.printall()
        return tmp.val
    
    def printall(self):
        res = []
        curr = self.head
        while curr is not None:
            res.append(curr.val)
            curr = curr.next
        print(res)
