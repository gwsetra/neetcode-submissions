class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1
        count = 0
        tmpl = None
        tmpr = None

        if len(s) <= 2:
            return True

        if len(set(s)) == len(s):
            return False
        
        def checksubpalindrome(substr):
            r = len(substr) - 1
            l = 0
            print('input subpalindrome', substr)
            while r > l:
                print(l,r)
                print(s[l], s[r])
                if s[r] != s[l]:
                    return False
                    
                r-=1
                l+=1

            return True
        
        while r>l:
            print(l,r)
            print(s[l], s[r])
            if s[r] != s[l]:
                print('inside if')
                if count > 0:
                    return False
                # if s[r-1] != s[l] and s[l+1] != s[r] and count > 0:
                #     return False
                
                if s[l+1] == s[r] and count == 0:
                    print('shift left only')
                    tmpl = l+2
                    tmpr = r-1
                    # checksubpalindrome(s[l+2:r-1])
                elif s[r-1] == s[l] and count == 0:
                    print('shift right only')
                    tmpl = l+1
                    tmpr = r-2
                    # checksubpalindrome(s[l+1:r-2])
                count += 1
                res = checksubpalindrome(s[tmpl:tmpr])
                if res is False:
                    return False

            r-=1
            l+=1
        return True