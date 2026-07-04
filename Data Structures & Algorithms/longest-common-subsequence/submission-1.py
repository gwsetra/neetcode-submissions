class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        counter = 0
        result = 0
        loop = 0
        while text1 and text2 and counter < len(text1):
            # print(1)
            # print(text1[counter])
            loc = text2.find(text1[counter])
            if loc > -1:
                # print(text2[:loc], text2[loc+1:])
                text2 = text2[:loc]+text2[loc+1:]
                text1 = text1[:0]  +text1[1:]
                counter = 0
                result +=1
            else:
                counter += 1
            print(text1)
            print(text2)
            # break
            loop +=1
        print(result)
        return result