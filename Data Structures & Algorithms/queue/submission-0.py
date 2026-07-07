class Deque:
    
    def __init__(self):
        self.q = deque() 

    def isEmpty(self) -> bool:
        return len(self.q) == 0

    def append(self, value: int) -> None:
        self.q.append(value)
        print(self.q)

    def appendleft(self, value: int) -> None:
        self.q.appendleft(value)
        print(self.q)

    def pop(self) -> int:
        return -1 if len(self.q) <= 0 else self.q.pop()

    def popleft(self) -> int:
        return -1 if len(self.q) <= 0 else self.q.popleft()
