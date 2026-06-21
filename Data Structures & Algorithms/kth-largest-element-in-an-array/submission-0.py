import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        lastpopped = -999
        loop = 0
        print(nums)
        heapq.heapify_max(nums)
        print(nums)

        while True:
            tmp = heapq.heappop_max(nums)

            loop +=1
            
            if loop == k:
                break
        return tmp
