class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1
        count = 0


        while r>l:
            print(l, r)
            if s[r] != s[l]:
                print('inside if')
                if count > 0:
                    return False
                # if s[r-1] != s[l] and s[l+1] != s[r] and count > 0:
                #     return False
                
                print(s[l+1] == s[r] and count == 0)
                print(s[r-1] == s[l] and count == 0)
                print((l+1) == (r-1))
                if s[l+1] == s[r] and count == 0:
                    l += 1
                    count += 1
                    continue
                elif s[r-1] == s[l] and count == 0:
                    r -= 1
                    count += 1
                    continue
                
                elif (l+1) == (r-1):
                    count += 1
                    return False
                
                else:
                    return False
                
            r-=1
            l+=1
        return True