class MovingAverage:

    def __init__(self, size: int):
        self.iter = 0
        self.size = size
        self.nums = [] * size
        self.sums = 0

    def next(self, val: int) -> float:
        # print(
        if len(self.nums) >= self.size:
            # print('inside')
            self.sums -= self.nums.pop(0)
            self.iter -= 1
            # print(self.sums)
            # print(self.nums)
        
        self.nums.append(val)
        self.sums += val
        self.iter += 1
        # print(self.sums)
        return self.sums / self.iter


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
