class Solution:
    def maxArea(self, heights: List[int]) -> int:
        lp = 0
        lr = len(heights) - 1

        cursum = min(heights[lp], heights[lr]) * lr-lp
        while lp < lr:

            cursum = max(min(heights[lp+1], heights[lr]) * (lr-(lp+1)), min(heights[lp], heights[lr-1]) * (lr-1-lp), cursum)
            print(cursum)
            lp += 1
            lr -= 1
        print(cursum)
        return cursum
