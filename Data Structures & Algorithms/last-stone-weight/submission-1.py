import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        loop =0
        max_heap = [-x for x in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1 and loop < 10:
            largest1 = -heapq.heappop(max_heap)
            largest2 = -heapq.heappop(max_heap)

            difference = abs(largest1 - largest2)
            if difference > 0:
                heapq.heappush(max_heap, -difference)

            
            loop+=1
        
        return 0 if len(max_heap) == 0 else -max_heap[0]