class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash = {}
        t_hash = {}

        for item in s:
            if item in s_hash:
                s_hash[item] += 1
            else:
                s_hash[item] = 1
        for item in t:
            if item in t_hash:
                t_hash[item] += 1
            else:
                t_hash[item] = 1
            
        # print(s_hash)
        # print(t_hash)
        return s_hash == t_hash