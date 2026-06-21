class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.max_row = len(grid)
        self.max_col = len(grid[0])
        counter = 0
        for loop1 in range(self.max_row):
            for loop2 in range(self.max_col):
                # print(loop1, loop2)
                # print(grid[loop1][loop2])
                # print(grid[loop1][loop2] == 1)
                if grid[loop1][loop2] == '1':
                    counter += self.dfs(grid, loop1, loop2)
                    # print('finished asoy')
        return counter
    
    def dfs(self, grid, row, column):
        # print('inside dfs :', row, column)
        # print('grid', grid)
        if ((min(row, column) < 0)
        or row == self.max_row or column == self.max_col or
        grid[row][column] == '0'):
            # print('unwanted place')
            return 0

        grid[row][column] = '0'

        self.dfs(grid, row-1, column) # atas
        self.dfs(grid, row, column +1) # kanan
        self.dfs(grid, row+1, column) # bawah
        self.dfs(grid, row, column-1) # kiri


        return 1


    
