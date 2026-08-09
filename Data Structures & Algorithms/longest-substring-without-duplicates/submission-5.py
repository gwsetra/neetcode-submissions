class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sets = set()
        l = 0
        longest = 0
        stringlen = len(s)

        for r in range(stringlen):
            if s[r] not in sets:
                sets.add(s[r])
            else:
                longest = max(longest, r-l)
                l = r
            
        print(longest)
        if stringlen == 1:
            return 1
        return max(longest, stringlen-l)
            