class MyStack:

    def __init__(self):
        self.stack = []
        self.head = None
        self.tail = None
        

    def push(self, x: int) -> None:
        if not self.stack: # if empty
            self.stack.append(x)
            self.head = 0
            self.tail = 0
        else:
            self.stack.append(x)
            self.tail += 1
        

    def pop(self) -> int:
        if self.tail == 0:
            val = self.stack.pop()
            self.head = None
            self.tail = None
        else:
            val = self.stack.pop(self.tail)
            self.tail -= 1
        return val

    def top(self) -> int:
        return self.stack[self.tail]

    def empty(self) -> bool:
        return False if self.stack else True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()