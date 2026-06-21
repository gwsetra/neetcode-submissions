import math, heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        result = []
        for loop in range(0, len(points)):
            distance = math.sqrt(points[loop][0]**2 + points[loop][1]**2)

            min_heap.append((distance, points[loop]))

        heapq.heapify(min_heap)

        for loop in range(0, k):
            result.append(heapq.heappop(min_heap)[1])
        
        return result