class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        maps = defaultdict(int)
        lenstr = len(s)

        for i in range(len(s)):
            maps[s[i]] += 1
        print(maps)
        # check odds
        if lenstr % 2 == 1:
            print('ODD')
            # print(len(maps), (lenstr/2)+1)
            if len(maps) == (lenstr//2)+1:
                return True
        # check even
        elif lenstr % 2 == 0:
            print('EVEN')
            if len(maps) == lenstr/2:
                return True
        return False