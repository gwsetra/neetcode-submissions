class Solution:
    def countElements(self, arr: List[int]) -> int:
        maps = defaultdict(int)
        prev = None
        cnt = 0

        for i in range(len(arr)):
            maps[arr[i]] += 1
        print(maps)
        

        for i in range(max(maps)+1):
            # print(i)
            print(i, maps[i])
            if prev is None:
                prev = (i, maps[i])
                continue
            
            if i-1 == prev[0] and prev[1] != 0 and maps[i] != 0:
                print('add')
                cnt += prev[1]
            
            prev = (i, maps[i])

        print(cnt)
        return cnt