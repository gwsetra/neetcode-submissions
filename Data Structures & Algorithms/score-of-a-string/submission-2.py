class Solution:
    def scoreOfString(self, s: str) -> int:
        sets = {}
        sums = 0

        for i in range(len(s)-1):
            if s[i] not in sets:
                sets[s[i]] = (ord(s[i]))
            if s[i+1] not in sets:
                sets[s[i+1]] = (ord(s[i+1]))
            asciileft = sets[s[i]]
            asciiright = sets[s[i+1]]

            # print(asciileft, asciiright)
            sums += abs(asciiright-asciileft)
        # print(sums)
    
        return sums