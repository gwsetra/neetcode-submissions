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
        print('*--------*')
        print('get: ', key)
        curr = self.head.next
        while curr != self.tail:
            # print(curr.key, curr.value)
            # if curr == self.tail:
            #     # print('get reached tail, element not found')
            #     return -1
            if curr.key == key:
                print('doing re position for ', curr.key, curr.value)
                self.remove_nth(curr)
                self.printlinkedlist()
                self.add_element(curr)
                self.printlinkedlist()

                return curr.value
            else:
                curr = curr.next
        return -1

    def put(self, key: int, value: int) -> None:
        print('put: ', key, value)

        tmp = self.Node(key, value)

        curr = self.head
        loop = 0
        while True :
            print('curr key', curr.key, key, value)
            if curr.next == self.tail and self.length == 0:
                # print('list empty')

                self.add_element(tmp)

                self.printlinkedlist()
                break
            elif key in self.lrucache:
                print('update existing element')
                self.remove_using_lrucache(key)
                self.printlinkedlist()
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
        print('start printing Node')
        curr = self.head
        while True:
            print(curr.key, curr.value)
            if curr.next is not None:
                # print('Next Node:')
                curr = curr.next
            else:
                break

    def remove_nth(self, curr):
        print('start remove_nth element')
        # curr = self.head.next
        curr.prev.next = curr.next
        curr.next.prev = curr.prev

        curr.prev = None
        curr.next = None

        self.length -= 1

        del self.lrucache[curr.key]
        print('value of self.lrucache', self.lrucache)
            
    def remove_first(self):
        # print('start removing element')
        curr = self.head.next
        self.head.next = curr.next
        curr.next.prev = self.head

        curr.prev = None
        curr.next = None

        self.length -= 1

        del self.lrucache[curr.key]
        print('value of self.lrucache', self.lrucache)
    
    def remove_using_lrucache(self, key):
        print('start remove_using_lrucache:')
        curr = self.lrucache[key]
        curr.prev.next = curr.next
        curr.next.prev = curr.prev

        curr.prev = None
        curr.next = None

        self.length -= 1

        del self.lrucache[curr.key]
        print('value of self.lrucache', self.lrucache)

    def add_element(self, curr):
        # print('start adding element')
        curr.next = self.tail
        curr.prev = self.tail.prev
        
        self.tail.prev.next = curr
        self.tail.prev = curr

        self.length += 1

        self.lrucache[curr.key] = curr 
        print('value of self.lrucache', self.lrucache)

    
            

