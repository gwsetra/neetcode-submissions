class LRUCache:
    class Node:
        def __init__(self, key, val):
            self.prev = None
            self.key = key
            self.value = val
            self.next = None

    def __init__(self, capacity: int):
        self.lrucache = {}
        self.capacity = capacity
        self.length = 0

        self.head = self.Node(None, None)
        self.tail = self.Node(None, None)

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        # print('*--------*')
        # print('get: ', key)
        curr = self.head.next
        while True:
            # print(curr.key, curr.value)
            if curr == self.tail:
                # print('get reached tail, element not found')
                return -1
            elif curr.key == key:
                # print('doing re position for ', curr.key, curr.value)
                self.remove_first()
                self.printlinkedlist()
                self.add_element(curr)
                self.printlinkedlist()

                return curr.value
            else:
                curr = curr.next 

    def put(self, key: int, value: int) -> None:
        # print('put: ', key, value)

        tmp = self.Node(key, value)

        curr = self.head
        loop = 0
        while True :
            if curr.next == self.tail and self.length == 0:
                # print('list empty')

                self.add_element(tmp)

                self.printlinkedlist()
                break    
            elif self.length < self.capacity:
                # print('inside 2nd else if', self.length, self.capacity)
                if curr.next != self.tail:
                    curr = curr.next
                    # break
                elif curr.next == self.tail:
                    self.add_element(tmp)
                    self.printlinkedlist()
                    break
            elif self.length >= self.capacity:
                # print('self.length > self.capacity', self.length, self.capacity)
                self.remove_first()
                self.printlinkedlist()
                self.add_element(tmp)
                self.printlinkedlist()
                break
            loop +=1

    def printlinkedlist(self):
        # print('start printing Node')
        curr = self.head
        while True:
            # print(curr.key, curr.value)
            if curr.next is not None:
                # print('Next Node:')
                curr = curr.next
            else:
                break

            
    def remove_first(self):
        # print('start removing element')
        curr = self.head.next
        self.head.next = curr.next
        curr.next.prev = self.head

        curr.prev = None
        curr.next = None

        self.length -= 1
        

    def add_element(self, curr):
        # print('start adding element')
        curr.next = self.tail
        curr.prev = self.tail.prev
        
        self.tail.prev.next = curr
        self.tail.prev = curr

        self.length += 1


    
            

