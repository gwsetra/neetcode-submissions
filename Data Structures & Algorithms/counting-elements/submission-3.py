class Solution:
    def countElements(self, arr: List[int]) -> int:
        maps = defaultdict(int)
        prev = None
        cnt = 0

        for i in range(len(arr)):
            maps[arr[i]] += 1
        # print(maps)
        

        for k, v in maps.items():
            # print(k, v)
            if prev is None:
                prev = (k, v)
                continue
            
            if k-1 == prev[0]:
                cnt += v
            
            prev = (k, v)
        
        return count