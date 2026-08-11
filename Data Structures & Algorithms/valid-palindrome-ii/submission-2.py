class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1
        count = 0

        while r>l:
            if s[r] != s[l]:
                count += 1
            if len(s) % 2 == 0 and count > 0:
                return False
            elif count > 1:
                return False
            r-=1
            l+=1
        return True