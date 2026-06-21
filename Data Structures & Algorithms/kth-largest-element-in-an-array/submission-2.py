import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.myheap = []

        for item in nums:
            if len(self.myheap) >= k-1:
                if item >= self.myheap[0]:
                    heapq.heappop(self.myheap)
            heapq.heappush(self.myheap, item)

        return heapq.heappop(self.myheap)