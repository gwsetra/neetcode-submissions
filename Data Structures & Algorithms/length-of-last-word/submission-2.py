class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        print(s)
        if len(s)==1:
            return 1
        for i in range(len(s)-1, -1, -1):
            if s[i] == ' ':
                break
        
        # print(len(s), i)
        return len(s)-1-i