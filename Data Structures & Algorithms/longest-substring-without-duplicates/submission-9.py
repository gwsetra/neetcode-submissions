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
                longest = max(longest, r-l)
                while True:
                    # print(sets)
                    sets.remove(s[l])
                    # print(sets)
                    l += 1
                    if s[r] not in sets:
                        sets.add(s[r])
                        break
            
        print(longest)
        if stringlen == 1:
            return 1
        return longest
            