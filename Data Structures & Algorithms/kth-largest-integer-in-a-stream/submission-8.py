import heapq

class KthLargest:
    heap = []
    maxs = 0
    def __init__(self, k: int, nums: List[int]):
        self.maxs = k
        print('maxs', self.maxs)
        for loop in range(0, len(nums)):
            self.heap.append(nums[loop])
        
        print(self.heap)
        heapq.heapify(self.heap)
        print(self.heap)

        # 3. Enforce the "Capacity of 3" rule
        while len(self.heap) > k:
            heapq.heappop(self.heap) # Kicks out the weakest person
        print(self.heap)

    def add(self, val: int) -> int:
        print('inside add')
        print(self.heap)
        print(self.maxs)
        heapq.heappush(self.heap, val)
        print(self.heap)
        
        while len(self.heap) > self.maxs:
            print('1')
            print(len(self.heap))
            heapq.heappop(self.heap) # Kicks out the weakest person
        print('after while', self.heap)
        return heapq.nsmallest(1, self.heap)[0]
