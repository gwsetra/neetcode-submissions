class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maps = defaultdict(int)
        l = 0
        strlen = len(s)
        wdwlen = 0
        currmax = None
        maxval = 0

        for r in range(strlen):
            # print(s[r])
            maps[s[r]] += 1
            # print(max(maps.values()))
            # print('currmax char',max(maps, key=maps.get))
            # print((r-l+1), max(maps.values()), k)
            if (r-l+1) - max(maps.values()) > k:
                print('inside IFF')
                # maxval = max(maxval, (r-l))
                maps[s[l]] -= 1
                l+=1
            maxval = (r - l + 1)

        return maxval if maxval > 0 else strlen