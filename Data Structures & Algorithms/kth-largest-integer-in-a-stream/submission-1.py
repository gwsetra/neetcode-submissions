class KthLargest:
    heap = []
    maxs = 0
    def __init__(self, k: int, nums: List[int]):
        global maxs
        print(self.heap)
        maxs = k

        for loop in range(0, len(nums)):
            self.heap.append(nums[loop])
            if len(self.heap) > k:
                self.heap.pop(0)

            print(self.heap)

    def add(self, val: int) -> int:
        self.heap.append(val)
        if len(self.heap) > maxs:
            self.heap.pop(0)
            return self.heap[0]
