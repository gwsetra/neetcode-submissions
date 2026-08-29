class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        lp=0
        lr=0

        # print(joined, lp, lr)

        while lp<len(s) and lr < len(t):
            # print(s[lp], t[lr])

            if s[lp] == t[lr]:
                lp += 1
                lr += 1
            else:
                lp += 1
        return (len(t) - lr)
        