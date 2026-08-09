class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sets = set()
        l = 0
        longest = 0

        for r in range(len(s)):
            if s[r] not in sets:
                sets.add(s[r])
            else:
                longest = max(longest, r-l)
                l = r
            
        print(longest)
        if len(s) == 1:
            return 1
        return longest
            