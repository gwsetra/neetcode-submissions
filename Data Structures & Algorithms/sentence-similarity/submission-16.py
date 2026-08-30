class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        cnt = 0
        combinedset = set(sentence1+sentence2)
        shortpairs = [pair for pair in similarPairs if set(pair).issubset(combinedset) ]
        print(combinedset, shortpairs)

        if (len(similarPairs) == 0 and sentence1 == sentence2) or sentence1 == sentence2:
            return True
        if len(sentence1) != len(sentence2):
            # print('here')
            return False
        else:
            print('here')
            for i in range(len(sentence1)):
                print([sentence1[i],sentence2[i]], [sentence2[i],sentence1[i]], shortpairs, [sentence1[i],sentence2[i]] in shortpairs, [sentence2[i],sentence1[i]] in shortpairs)
                if sentence1[i] == sentence2[i]:
                    continue
                elif not ([sentence1[i],sentence2[i]] in shortpairs or [sentence2[i],sentence1[i]] in shortpairs):
                    return False
        return True