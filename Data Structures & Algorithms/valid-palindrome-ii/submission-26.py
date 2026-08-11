class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1
        count = 0

        if len(s) <= 2:
            return True

        if len(set(s)) == len(s):
            return False
        
        def checksubpalindrome(substr):
            r = len(substr) - 1
            l = 0
            while r > l:
                if substr[r] != substr[l]:
                    return False
                r-=1
                l+=1

            return True
        
        while r>l:
            if s[r] != s[l]:
                if count > 0:
                    return False
                count += 1
                res = checksubpalindrome(s[l:r-1+1]) or checksubpalindrome(s[l+1:r+1])
                if res is False:
                    return False
                else: 
                    return True

            r-=1
            l+=1
        return True