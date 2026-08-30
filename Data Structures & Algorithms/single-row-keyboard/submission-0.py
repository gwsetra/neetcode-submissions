class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        maps = defaultdict(dict)
        rangesum = 0
        prev = 0

        for i in range(len(keyboard)):
            maps[keyboard[i]] = i
        
        # print(maps)
        for i in range(len(word)):
            # print(maps[word[i]])
            rangesum += abs(maps[word[i]]-prev)
            prev = maps[word[i]]
        # print(rangesum)
        return rangesum