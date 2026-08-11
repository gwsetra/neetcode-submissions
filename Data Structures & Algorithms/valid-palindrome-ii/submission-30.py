class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1
        
        def checksubpalindrome(x, y):
            # print('inside palindrome')
            if y > len(s)-1:
                y = len(s)-1
            while y > x:
                if s[y] != s[x]:
                    return False
                y-=1
                x+=1

            return True
        
        while r>l:
            if s[r] != s[l]:
                res = checksubpalindrome(l, r-1) or checksubpalindrome(l+1, r)
                # print(checksubpalindrome(l, r-1+1), checksubpalindrome(l+1, r+1) )
                # print(res)
                if res is False:
                    return False
                else: 
                    return True

            r-=1
            l+=1
        return True