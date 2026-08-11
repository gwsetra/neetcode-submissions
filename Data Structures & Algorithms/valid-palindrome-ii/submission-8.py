class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1
        count = 0


        while r>l:
            if s[r] != s[l]:
                print('inside if')
                if count > 0:
                    return False
                # if s[r-1] != s[l] and s[l+1] != s[r] and count > 0:
                #     return False
                count += 1
                if s[l+1] == s[r] and count == 0:
                    l += 1
                    continue
                elif s[r-1] == s[l] and count == 0:
                    r -= 1
                    continue
                
            r-=1
            l+=1
        return True