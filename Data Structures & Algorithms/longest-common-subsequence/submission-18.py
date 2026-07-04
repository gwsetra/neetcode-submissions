class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        p1 = p2 = 0
        text1 = '?'+text1
        text2 = '!'+text2
        maxrow = len(text1)
        maxcol = len(text2)
        prev = [0] * (maxcol)
        # print(text1, text2, prev)

        for lrow in range(maxrow):
            curr = [0] * (maxcol)

            for lcol in range(0, maxcol):
                # print(lrow, lcol)
                # print(text1[lrow], text2[lcol])
                if text1[lrow] == text2[lcol]:
                    # print('match found')
                    curr[lcol] = prev[lcol-1] + 1
                else:
                    curr[lcol] = max(prev[lcol], curr[lcol-1])
            # print(prev, curr)
            prev = curr
            
        return curr[maxcol-1]