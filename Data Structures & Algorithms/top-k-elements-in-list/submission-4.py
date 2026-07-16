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
            if bucket[item]==0 or bucket[item]== []:
                continue
            # print(item)
            # print(bucket[item])
            if len(bucket[item]) == 1:
                # print(bucket[item])
                res.append(bucket[item][0])
            else:
                res.append(bucket[item])
            # print(bucket, bucket[item])
            
        return res