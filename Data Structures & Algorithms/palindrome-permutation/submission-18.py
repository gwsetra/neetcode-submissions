class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        maps = defaultdict(int)
        summap = 0
        cnt = 0

        for i in range(len(s)):
            maps[s[i]] += 1
        # print(maps)

        for item in maps.items():
            # print(item)
            if item[1] %2==1:
                cnt +=1
                if cnt > 1:
                    return False

        return True