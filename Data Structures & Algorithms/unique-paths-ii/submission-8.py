class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        maxrow = len(obstacleGrid)
        maxcol = len(obstacleGrid[0])
        prev = [0] * maxcol
        # print(prev)

        if obstacleGrid[0][0] == 1:
            return 0

        for lx in range(maxrow):
            curr = [0] * maxcol
            if lx == 0:
                curr[0] = 1
            else:
                curr[0] = prev[0] if obstacleGrid[lx][0] != 1 else 0


            for ly in range(1, maxcol):
                # print(lx, ly)
                if obstacleGrid[lx][ly] == 1:
                    curr[ly] = 0
                    continue
                # print(prev)
                curr[ly] = curr[ly-1] + prev[ly]
            prev = curr
            # print(curr)
        
        return curr[maxcol-1]