class MinStack:

    def __init__(self):
        self.stack = []
        self.sorted_tmp = []

    def push(self, val: int) -> None:
        if self.sorted_tmp == [] or val <= self.sorted_tmp[-1]:
            self.sorted_tmp.append(val)
        
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack[-1] == self.sorted_tmp[-1]:
            self.sorted_tmp.pop()
        
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.sorted_tmp[-1]
        
