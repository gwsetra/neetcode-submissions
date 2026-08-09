class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sets = set()
        l = 0
        longest = 0
        stringlen = len(s)

        for r in range(stringlen):
            # print('--**---')
            # print(r, l)
            if s[r] not in sets:
                sets.add(s[r])
            else:
                # print(r, l)
                longest = max(longest, r-l)
                l = r
                sets = set()
                sets.add(s[l])
                # print(r, l)
            
        print(longest)
        if stringlen == 1:
            return 1
        return max(longest, stringlen-l)
            