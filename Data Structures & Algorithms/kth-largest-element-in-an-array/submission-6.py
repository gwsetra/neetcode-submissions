import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        myheap = []

        for item in nums:
            # print('before',self.myheap)
            if len(myheap) >= k:
                if item >= myheap[0]:
                    heapq.heappop(myheap)
                    heapq.heappush(myheap, item)
            else:
                heapq.heappush(myheap, item)
            # print('after',self.myheap)

        return heapq.heappop(myheap)