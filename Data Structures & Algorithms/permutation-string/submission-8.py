class Solution:
    # optimised solution
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts1 = [0] * 26
        counts2 = [0] * 26
        s1counter = 0
        # print(ord('a'))
        if len(s2) > len(s1):
            for i in range(len(s1)):
                counts1[ord(s1[i])-ord('a')] += 1
            print(counts1)
            for i in range(len(s2)):
                if i >= len(s1):
                    print('start popping up')
                    counts2[ord(s2[i-len(s1)])-ord('a')] -= 1
                counts2[ord(s2[i])-ord('a')] += 1
                print(counts2)
                if counts1 == counts2:
                    return True
        return False
        # for i in range(len(s2)):
        #     if i >= len(s1):
        #         print('start popping up')
        #         counts2[ord(s2[i-len(s1)])-ord('a')] -= 1
        #     # print(i, ord(s1[min(i, len(s1)-1)]), ord(s2[i]))
        #     if s1counter < len(s1):
        #         counts1[ord(s1[i])-ord('a')] += 1
        #     counts2[ord(s2[i])-ord('a')] += 1
        #     s1counter += 1
        #     print(counts1)
        #     print(counts2)
        #     if (counts1 == counts2 and i >= len(s1)):
        #         return True
        # if counts1 == counts2:
        #     return True
        # return False