class Solution:
    def scoreOfString(self, s: str) -> int:
        sets = {}
        sums = 0

        for i in range(len(s)-1):
            # print(asciileft, asciiright)
            sums += abs(ord(asciiright)-ord(asciileft))
        # print(sums)
    
        return sums