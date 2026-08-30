class Solution:
    def confusingNumber(self, n: int) -> bool:
        maps = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
        char = str(n)
        flags = False
        newstr = ''

        if len(char)==1:
            return True if (char[0] in maps) and char[0] not in ('0', '1', '8') else False

        for i in range(len(char)-1, -1, -1):
            print(char[i])

            if char[i] not in maps:
                return False
            else:
                print(maps[char[i]], char[len(char)-1-i])
                if len(char)%2 == 1 and len(char) // 2 == i:
                    continue
                if maps[char[i]] == char[len(char)-1-i]:
                    return False
            
        return True
