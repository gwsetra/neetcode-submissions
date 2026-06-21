import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.myheap = []

        for item in nums:
            # print('before',self.myheap)
            if len(self.myheap) >= k:
                if item >= self.myheap[0]:
                    heapq.heappop(self.myheap)
                    heapq.heappush(self.myheap, item)
            else:
                heapq.heappush(self.myheap, item)
            # print('after',self.myheap)

        return heapq.heappop(self.myheap)