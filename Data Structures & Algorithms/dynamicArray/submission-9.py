class DynamicArray:
    
    def __init__(self, capacity: int):
        self.arr = [None] * capacity
        self.arrlen = capacity
        self.last = 0
        

    def get(self, i: int) -> int:
        # print('inside get', i)
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        # print('self set', i, n)
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        # print('inside pushback', n)
        if self.last == 0:
            self.arr[0] = n
        elif self.last < self.arrlen:
            self.arr[self.last] = n
        else:
            self.resize()
            self.arr[self.last] = n
            # self.arr.append(n)
        self.last += 1

        # print(self.arr)

    def popback(self) -> int:
        # print('inside popback')
        tmp = self.arr[self.last-1]
        self.arr[self.last-1] = None
        self.last -= 1
        return tmp

    def resize(self) -> None:
        # print('resizing')
        self.arr += [None]*self.last
        # print('self.arr', self.arr)
        self.arrlen = len(self.arr)

    def getSize(self) -> int:
        # print('inside getSize')
        # counter = 0
        # for item in self.arr:
        #     counter += 1 if item is not None else 0
        # return counter
        return self.last
    
    def getCapacity(self) -> int:
        # print('inside getCapacity ')
        # print(self.arr)
        return self.arrlen