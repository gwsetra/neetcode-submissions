class Node():
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head  = Node(None)
        self.tail = self.head
        self.length = 0
    
    def get(self, index: int) -> int:
        curr = 0
        if index > self.length-1:
            return -1
        elif index == 0:
            return self.head.next.val
        elif index == self.length-1:
            return self.tail.val
        else:
            tmp = self.head
            while curr <= index:
                tmp = tmp.next
                curr += 1
            return tmp.val


    def insertHead(self, val: int) -> None:
        # print('insert head', val)
        nnode = Node(val)

        if self.tail == self.head: # if list empty:
            self.head.next = nnode
            self.tail = nnode
        else:
            nnode.next = self.head.next
            self.head.next = nnode
        self.length += 1
        # self.getValues()


    def insertTail(self, val: int) -> None:
        # print('insert tail', val)
        nnode = Node(val)

        if self.tail == self.head: # if list empty:\
            # print('asdf')
            self.head.next = nnode
            self.tail = nnode
        else:
            self.tail.next = nnode
            self.tail = nnode
        self.length += 1
        # self.getValues()

    def remove(self, index: int) -> bool:
        # print('inside remove idx', index)
        curr = 0
        if index > self.length-1:
            self.getValues()
            return False
        elif index == 0:
            self.head = self.head.next
        elif index == self.length-1:
            tmp = self.head
            while tmp.next != self.tail:
                tmp = tmp.next
            self.tail = tmp
            self.tail.next = None
        else:
            tmp = self.head
            while curr < index:
                tmp = tmp.next
                curr += 1
            tmp.next = tmp.next.next
        self.length -= 1
        # self.getValues()
        return True
            
        

    def getValues(self) -> List[int]:
        # print('inside getValues')
        result = []
        curr = self.head.next
        loop = 0
        if self.length == 0:
            return result

        while curr is not None:
            result.append(curr.val)
            curr = curr.next
            loop += 1

        # print(result)
        return result
