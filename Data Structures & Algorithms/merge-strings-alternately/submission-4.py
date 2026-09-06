class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l = 0
        r = 0
        new = ''
        word1len = len(word1)
        word2len = len(word2)
        longest = min(word1len, word2len)
        biggest = 1 if word2len > word1len else 0
        # print(longest, biggest)

        for i in range(longest):
            new += (word1[i] + word2[i])
        # print(new)


        # print(new)
        return new + word1[longest:] + word2[longest:]