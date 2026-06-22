class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(row, column):
            # print('inside dfs')
            # print(row, column)
            # print('current value', grid[row][column])   
            if (min(row, column) < 0 or
            row == rowlen or column == columnlen or
            grid[row][column] == 0):
                return 0
            
            grid[row][column] = 0
            tmp_result = 1

            direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]
            
            for nr, nc in direction:
                tmp_result += dfs(row + nr, column + nc)
            
            return tmp_result
            


        max_result = 0
        rowlen = len(grid)
        columnlen = len(grid[0])

        for loop1 in range(0, rowlen):
            for loop2 in range(0, columnlen):
                if grid[loop1][loop2] == 1:
                    max_result = max(max_result, dfs(loop1, loop2))

                    # max_result = tmp if tmp > max_result else max_result
        return max_result