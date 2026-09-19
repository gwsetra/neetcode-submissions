class Solution:
    def maxArea(self, heights: List[int]) -> int:
        lp = 0
        lr = len(heights) - 1

        cursum = min(heights[lp], heights[lr]) * lr-lp
        while lp < lr:
            # print(lp, lr)
            cursum = max( min(heights[lp], heights[lr]) * (lr-(lp)), cursum)
            # cursum = max(min(heights[lp+1], heights[lr]) * (lr-(lp+1)), min(heights[lp], heights[lr-1]) * (lr-1-lp), min(heights[lp], heights[lr]) * (lr-(lp)), cursum)
            # print(cursum)
            if heights[lp] < heights[lr]:
                lp += 1
            elif heights[lr] < heights[lp]:
                lr -= 1
            else:
                lp += 1
                lr -= 1
        # print(cursum)
        return cursum
