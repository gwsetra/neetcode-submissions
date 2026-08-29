class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        lenelem = len(words[0])
        for x in range(1, len(words)):
            for y in range(0, min(x, len(words[x]))):
                print(x,y)
                if words[x][y] != words[y][x]:
                    return False
        return True
                