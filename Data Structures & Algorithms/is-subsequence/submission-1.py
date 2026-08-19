class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sp = 0
        rp = 0
        if s=='':
            return True

        while rp < len(t):
            # print(sp, rp)
            if t[rp] == s[sp]:
                sp += 1
                rp += 1
                continue
            rp += 1
        
        return sp==len(s)
            