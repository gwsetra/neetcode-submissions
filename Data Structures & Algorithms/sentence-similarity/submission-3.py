class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        len1 = sum(len(lens) for lens in sentence1)
        len2 = sum(len(lens) for lens in sentence2)
        lenall = sum(len(lens2)   for lens in similarPairs for lens2 in lens)
        print(len1, len2, lenall)

        if len(sentence1) != len(sentence2):
            return False
        else:
            for i in range(len(similarPairs)):
                if (similarPairs[i][0] == sentence1[i] or similarPairs[i][0] == sentence2[i]) and (similarPairs[i][1] == sentence1[i] or similarPairs[i][1] == sentence2[i]):
                    continue
                else:
                    return False
        return True