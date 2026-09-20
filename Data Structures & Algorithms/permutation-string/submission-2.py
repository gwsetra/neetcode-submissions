class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1map = defaultdict(int)
        s2map = defaultdict(int)
        for i in range(len(s1)):
            s1map[s1[i]] += 1
        
        # print(s1map)

        for i in range(len(s2)):
            if i > len(s1)-1:
                s2map[s2[i-len(s1)]] -= 1

                if s2map[s2[i-len(s1)]] == 0:
                    del s2map[s2[i-len(s1)]]
            s2map[s2[i]] += 1
            # print(s2[i], s2map, s1map == s2map)
            if s1map == s2map:
                return True
        return False