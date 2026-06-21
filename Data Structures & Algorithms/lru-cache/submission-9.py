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
        # print('inside get:', key)
        if key in self.lrucache:
            popped = self.remove_using_lrucache(key)
            # self.printlinkedlist()
            self.add_element(popped)
            # self.printlinkedlist()

            return self.lrucache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        tmp = self.Node(key, value)

        curr = self.head
        if key in self.lrucache:
            # print('updating existing value')
            self.remove_using_lrucache(key)
            # self.printlinkedlist()
            self.add_element(tmp)
            # self.printlinkedlist()
        elif self.length < self.capacity:
            self.add_element(tmp)
            # self.printlinkedlist()
        else:
            self.remove_first()
            # self.printlinkedlist()
            self.add_element(tmp)
            # self.printlinkedlist()

    def printlinkedlist(self):
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

        del self.lrucache[curr.key]
    
    def remove_using_lrucache(self, key):
        curr = self.lrucache[key]
        curr.prev.next = curr.next
        curr.next.prev = curr.prev

        curr.prev = None
        curr.next = None

        self.length -= 1

        del self.lrucache[curr.key]
        return curr

    def add_element(self, curr):
        # print('start adding element')
        curr.next = self.tail
        curr.prev = self.tail.prev
        
        self.tail.prev.next = curr
        self.tail.prev = curr

        self.length += 1

        self.lrucache[curr.key] = curr 

    
            

