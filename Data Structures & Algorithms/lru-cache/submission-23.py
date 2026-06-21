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

        self.head = self.Node(None, None)
        self.tail = self.Node(None, None)

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        # print('---???--')
        # self.printlinkedlist()
        # print('inside get:', key)
        if key in self.lrucache:
            # print('self.lrucache', self.lrucache)
            # print('self.lrucache[key]', self.lrucache[key])
            # print('self.lrucache[key].value', self.lrucache[key].value)
            self.move_to_tail(self.lrucache[key])
            # self.printlinkedlist()
            # self.add_element(popped.key, popped.value)
            # self.printlinkedlist()
            # print(self.lrucache[key])

            return self.lrucache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        # print('inside put:', key, value)
        curr = self.head
        if key in self.lrucache:
            # print('updating existing value', key, value)
            # self.remove_using_lrucache(key)
            # self.printlinkedlist()
            # self.add_element(key, value)
            node = self.update_node_value(self.lrucache[key], value)
            self.move_to_tail(node)
            # self.printlinkedlist()
        elif len(self.lrucache) < self.capacity:
            # print('self length < self.capacity')
            # self.printlinkedlist()
            tmpnode = self.create_new_node(key, value)
            self.add_to_tail(tmpnode)
            # self.add_element(key, value)
            # self.printlinkedlist()
        else:
            # print('element to put longer than what available')
            # self.printlinkedlist()
            self.delink(self.head.next)
            # self.printlinkedlist()
            tmpnode = self.create_new_node(key, value)
            self.add_to_tail(tmpnode)
            # self.printlinkedlist()
            # self.remove_first()
            # self.printlinkedlist()
            # self.add_element(key, value)
            # self.printlinkedlist()

    def printlinkedlist(self):
        # print('inside printlinkedlist')
        curr = self.head
        while True:
            # print(curr.key, curr.value)
            if curr.next is not None:
                # print('Next Node:')
                curr = curr.next
            else:
                break


    def update_node_value(self, node, value):
        # print('update node value')
        node.value = value

        return node
    
    def create_new_node(self, key, value):
        return self.Node(key, value)
    
    def move_to_tail(self, node):
        self.delink(node)
        self.add_to_tail(node)
    
    def delink(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

        node.next = None
        node.prev = None

        del self.lrucache[node.key]
    
    def add_to_tail(self, node):
        node.next = self.tail
        node.prev = self.tail.prev

        node.prev.next = node
        self.tail.prev = node

        self.lrucache[node.key] = node
            

