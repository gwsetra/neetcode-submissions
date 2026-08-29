class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        lenelem = len(words[0])
        pl = [1, 0]


        if len(words)==1 and len(words[0]) ==1:
            return True
        else:
            while pl[0] < (len(words)-1) and pl[1] < (len(words[0])-1):
                if pl[0] == pl[1]: # shift left down when in the middle
                    pl[0] += 1
                    pl[1] = 0 
                    continue
                
                # print(words[pl[0]][pl[1]], words[pl[1]][pl[0]])
                if words[pl[0]][pl[1]] != words[pl[1]][pl[0]]:
                    return False
                
                pl[1] = pl[1] + 1

        return True
                