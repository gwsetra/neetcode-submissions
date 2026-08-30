class Solution:
    def confusingNumber(self, n: int) -> bool:
        maps = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
        char = str(n)
        flags = False
        newstr = ''

        for i in range(len(char)-1, -1, -1):
            # print()
            if char[i] not in maps:
                return False
            if char[i] in ('6','9'):
                flags = True
            newstr += maps[char[i]]

        return newstr != char