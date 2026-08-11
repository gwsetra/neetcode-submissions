class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = 0
        r = len(s)-1
        while r > l :
            # print('loop')
            # print(s[l], s[r])
            tmp = s[l]
            s[l] = s[r]
            s[r] = tmp
            r-=1
            l+=1
        # print(s)