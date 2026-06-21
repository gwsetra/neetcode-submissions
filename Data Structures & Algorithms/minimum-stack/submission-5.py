class MinStack:

    def __init__(self):
        self.stack = []
        self.sorted_tmp = []

    def push(self, val: int) -> None:
        print('inside push')
        print(self.sorted_tmp)
        print(val)
        if self.sorted_tmp == [] or val < self.sorted_tmp[-1]:
            self.sorted_tmp.append(val)
        
        self.stack.append(val)
        print(self.stack)

    def pop(self) -> None:
        print('inside pop')
        if self.stack[-1] == self.sorted_tmp[-1]:
            self.sorted_tmp.pop()
        
        return self.stack.pop()

    def top(self) -> int:
        print('inside top')
        return self.stack[-1]
        

    def getMin(self) -> int:
        print('inside getMin')
        print(self.sorted_tmp[-1])
        return self.sorted_tmp[-1]
        
