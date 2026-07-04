class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache = {}

        def dfs(txt1, txt2):
            # print('txt1 txt2', txt1, txt2)
            if len(txt2) == 0 :
                # print('txt2 is None')
                return 0
            if len(txt2) and len(txt1) == 0:
                # print('returning 0')
                return 0
            if (txt1, txt2) in cache:
                return cache[(txt1, txt2)]
            
            if txt1[0] == txt2[0]:
                # print('element find', txt1[0])
                max_result = 1 + dfs(txt1[1:], txt2[1:])
                # print('max_result', max_result)
                # print('returning from txt1 txt2', txt1, txt2)
                cache[(txt1, txt2)] = max_result
                return max_result
            else:
                max_result = max(dfs(txt1[1:], txt2), dfs(txt1, txt2[1:]))
                cache[(txt1, txt2)] = max_result
                return max_result
            

            return 0

        return dfs(text1, text2)