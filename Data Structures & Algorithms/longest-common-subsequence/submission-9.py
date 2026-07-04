class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache = {}

        def dfs(text1, text2):
            # print('txt1 txt2', txt1, txt2)
            if len(text2) == 0 :
                # print('txt2 is None')
                return 0
            if len(text2) and len(text1) == 0:
                # print('returning 0')
                return 0
            if (text1, text2) in cache:
                return cache[(text1, text2)]
            
            if text1[0] == text2[0]:
                # print('element find', txt1[0])
                max_result = 1 + dfs(text1[1:], text2[1:])
                # print('max_result', max_result)
                # print('returning from txt1 txt2', txt1, txt2)
                cache[(text1, text2)] = max_result
                return max_result
            else:
                max_result = max(dfs(text1[1:], text2), dfs(text1, text2[1:]))
                cache[(text1, text2)] = max_result
                return max_result
            

            return 0

        return dfs(text1, text2)