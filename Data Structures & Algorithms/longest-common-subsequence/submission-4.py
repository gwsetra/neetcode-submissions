class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        def dfs(txt1, txt2, counter):
            # print('txt1 txt2', txt1, txt2)
            if len(txt2) == 0 :
                # print('txt2 is None')
                return 1
            if len(txt2) and len(txt1) == 0:
                return 0
            
            loc = txt2.find(txt1[0])
            
            if loc > -1:
                # print('element find', txt1[0])
                max_result = max(dfs(txt1[1:], txt2[loc+1:], 1), dfs(txt1[1:], txt2, 0))
                # print('max_result', max_result)
                # print('returning from txt1 txt2', txt1, txt2)
                counter += max_result
            else:
                counter += dfs(txt1[1:], txt2[loc+1:], 0)
            

            return counter

        return dfs(text1, text2, 0)