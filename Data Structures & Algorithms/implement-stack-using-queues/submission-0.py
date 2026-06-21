class MyStack:

    def __init__(self):
        self.stack = []
        self.head = None
        self.tail = None
        

    def push(self, x: int) -> None:
        print('push')
        if not self.stack: # if empty
            self.stack.append(x)
            self.head = 0
            self.tail = 0
        else:
            self.stack.append(x)
            self.tail += 1
        print(self.stack)
        

    def pop(self) -> int:
        print('pop')
        if self.tail == 0:
            val = self.stack.pop()
            self.head = None
            self.tail = None
        else:
            print(self.stack)
            print(self.tail)
            val = self.stack.pop(self.tail)
            print(val)
            self.tail -= 1
        return val

    def top(self) -> int:
        print('top')
        return self.stack[self.tail]

    def empty(self) -> bool:
        print('empty')
        print(self.stack)
        return False if self.stack else True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()