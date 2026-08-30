class Solution:
    def confusingNumber(self, n: int) -> bool:
        maps = {'1':'1', '6':'9', '8':'8', '9':'6'}
        char = str(n)
        flags = False

        for i in range(len(char)):
            # print()
            if char[i] not in maps:
                return False
            if char[i] in ('6','9'):
                flags = True
        
        return flags