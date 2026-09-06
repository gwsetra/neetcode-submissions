class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l = 0
        r = 0
        new = ''
        longest = min(len(word1), len(word2))
        biggest = 1 if len(word2) > len(word1) else 0
        # print(longest, biggest)

        for i in range(longest):
            new += (word1[i] + word2[i])
        # print(new)

        if biggest == 0:
            new += word1[i+1:]
        else:
            new += word2[i+1:]
        print(new)
        return new