class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        cnt = 0

        if len(similarPairs) == 0 and sentence1 == sentence2:
            return True
        if len(sentence1) != len(sentence2):
            # print('here')
            return False
        else:
            for iters in range(len(sentence1)):
                for i in range(len(similarPairs)):
                    # print(similarPairs[i])
                    if sentence1[iters] == sentence2[iters]:
                        cnt+=1
                        # print('found')
                        break
                    if (similarPairs[i][0] == sentence1[iters] or similarPairs[i][0] == sentence2[iters]) and (similarPairs[i][1] == sentence1[iters] or similarPairs[i][1] == sentence2[iters]):
                        print('found')
                        cnt+=1
                        break
        return cnt == len(sentence1)