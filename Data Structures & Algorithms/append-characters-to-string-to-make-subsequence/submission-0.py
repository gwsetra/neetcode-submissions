class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        rlen = len(t)
        cntsame = 0
        lp=0
        lr=len(s)

        joined = s+t
        # print(joined, lp, lr)

        while lp<len(s) and lr < len(joined):
            # print(s[lp], joined[lr])

            if s[lp] == joined [lr]:
                lp += 1
                lr += 1
            else:
                lp += 1
        return (len(joined) - lr)
        