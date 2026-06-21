import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.maxs = k

        for loop in range(0, len(nums)):
            self.heap.append(nums[loop])

        heapq.heapify(self.heap)

        # 3. Enforce the "Capacity of 3" rule
        while len(self.heap) > k:
            heapq.heappop(self.heap) # Kicks out the weakest person


    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        
        while len(self.heap) > self.maxs:
            heapq.heappop(self.heap) # Kicks out the weakest person
        return heapq.nsmallest(1, self.heap)[0]
