class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort
        count = {}
        bucket = [[] for i in range(len(nums) + 1)]
        res = []

        for item in nums:
            count[item] = 1 + count.get(item, 0)
        
        print(count, bucket)
        for key, value in count.items():

            bucket[value].append(key)
        print(bucket)
        print(count, len(count))
        print(bucket)

        for item in range(len(bucket)-1, len(count)-k, -1):
            if bucket[item]== []:
                continue
            for item2 in bucket[item]:
                res.append(item2)
            if len(res) == k:
                return res
            
        return res