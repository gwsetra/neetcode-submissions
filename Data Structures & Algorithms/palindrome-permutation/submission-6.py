class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        maps = defaultdict(int)
        summap = 0
        lenstr = len(s)

        for i in range(len(s)):
            maps[s[i]] += 1
        print(maps)
        summap += sum(val[1] for val in maps.items())
        # check odds
        if lenstr % 2 == 1 and len(maps) <= (lenstr//2)+1:
            print('ODD')
            # print(len(maps), (lenstr/2)+1)
            
            # print(summap)
            # if len(maps) == (lenstr//2)+1:
            #     return True
            if summap == lenstr:
                return True
        # check even
        elif lenstr % 2 == 0 and len(maps) < (lenstr//2)+1:
            print('EVEN')
            if len(maps) == lenstr/2:
                # print('here')
                return True
            
            # if summap == lenstr:
            #     print('here1')
            #     return True
        return False