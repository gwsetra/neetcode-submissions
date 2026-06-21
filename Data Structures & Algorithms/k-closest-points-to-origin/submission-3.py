import math, heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        result = []
        for x, y in points:
            distance = math.sqrt(x**2 + y**2)

            min_heap.append((distance, [x, y]))

        heapq.heapify(min_heap)

        for _ in range(0, k):
            result.append(heapq.heappop(min_heap)[1])
        
        return result