class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        maps = {}

        for x in nums:
            if x not in maps:
                maps[x] = 1
            else:
                maps[x] += 1
        # print(maps)
        sorted_x = sorted(maps.items(), key=lambda kv: kv[1], reverse=True)
        keys_only = [k for k, v in sorted_x]
        return keys_only[:k]