class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        lenelem = len(words[0])
        pl = [1, 0]


        if len(words)==1 and len(words[0]) ==1:
            print(1)
            return True
        else:
            while pl[0] < len(words):
                # print(len(words[pl[0]-1]), len(words[pl[0]]))
                if len(words[pl[0]-1]) >= len(words[pl[0]]):
                    print(pl)
                    if pl[0] == pl[1]:
                        pl[0] += 1
                        pl[1] = 0
                    else:
                        colvalue = [row for row in words[pl[0]]]
                        # print(words[pl[0]])
                        # print(colvalue)
                        if len(words[pl[0]]) == len(colvalue) and pl[1] < len(words[pl[0]]) and words[pl[0]][pl[1]] != words[pl[1]][pl[0]]:
                            print(2)
                            return False
                    pl[1] += 1
                else:
                    print(3)
                    return False

        return True
                