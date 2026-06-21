class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash = {}
        t_hash = {}
        if len(s) != len(t):
            return False

        for loop in range(len(s)):
            s_hash[s[loop]] = 1 + s_hash.get(s[loop], 0)
            t_hash[t[loop]] = 1 + t_hash.get(t[loop], 0)
            
        # print(s_hash)
        # print(t_hash)
        return s_hash == t_hash