class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort
        count = {}
        bucket = [0] * (len(nums)+1)
        res = []

        for item in nums:
            count[item] = 1 + count.get(item, 0)
        
        print(count, bucket)
        for item in count.items():
            bucket[item[1]].append(item[0])
        print(count, len(count))
        print(bucket)

        for item in range(len(bucket)-1, len(count)-k, -1):
            if bucket[item]==0:
                continue
            print(item)
            print(bucket[item])
            # print(bucket, bucket[item])
            res.append(bucket[item])
        return res