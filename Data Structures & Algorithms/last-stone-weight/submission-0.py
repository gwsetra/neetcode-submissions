import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        loop =0
        max_heap = [-x for x in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1 and loop < 10:
            print('-------')
            print(max_heap)
            largest1 = -heapq.heappop(max_heap)
            largest2 = -heapq.heappop(max_heap)

            print(largest1, largest2)

            difference = abs(largest1 - largest2)
            if difference > 0:
                heapq.heappush(max_heap, -difference)
            print(max_heap)
            
            loop+=1
        
        print(0 if len(max_heap) == 0 else -max_heap[0])
        return 0 if len(max_heap) == 0 else -max_heap[0]