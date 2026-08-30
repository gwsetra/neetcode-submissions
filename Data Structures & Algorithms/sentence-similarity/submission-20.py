class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        cnt = 0
        combinedset = set(sentence1+sentence2)
        shortpairs = [set(pair) for pair in similarPairs if set(pair).issubset(combinedset) ]

        if (len(similarPairs) == 0 and sentence1 == sentence2) or sentence1 == sentence2:
            return True
        if len(sentence1) != len(sentence2):
            # print('here')
            return False
        else:
            for i in range(len(sentence1)):
                if sentence1[i] == sentence2[i]:
                    continue
                elif (set([sentence1[i],sentence2[i]]) not in shortpairs):
                    return False
        return True