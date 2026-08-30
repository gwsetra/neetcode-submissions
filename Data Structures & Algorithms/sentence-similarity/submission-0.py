class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        for i in range(len(similarPairs)):
            # print(similarPairs[i])
            # print(similarPairs[i][0] != sentence1[i] and similarPairs[i][0] != sentence2[i])
            # print(similarPairs[i][1] != sentence1[i] and similarPairs[i][1] != sentence2[i])
            if (similarPairs[i][0] != sentence1[i] and similarPairs[i][0] != sentence2[i]) and (similarPairs[i][1] != sentence1[i] and similarPairs[i][1] != sentence2[i]):
                return False
        return True