class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        max_row = len(grid)
        max_col = len(grid[0])
        counter = 0
        def dfs(row, column):
            # print('inside dfs :', row, column)
            # print('grid', grid)
            if ((min(row, column) < 0)
            or row == max_row or column == max_col or
            grid[row][column] == '0'):
                # print('unwanted place')
                return 

            grid[row][column] = '0'

            dfs(row-1, column) # atas
            dfs(row, column +1) # kanan
            dfs(row+1, column) # bawah
            dfs(row, column-1) # kiri


        for loop1 in range(max_row):
            for loop2 in range(max_col):
                # print(loop1, loop2)
                # print(grid[loop1][loop2])
                # print(grid[loop1][loop2] == 1)
                if grid[loop1][loop2] == '1':
                    counter += 1
                    dfs(loop1, loop2)
                    # print('finished asoy')
        return counter
    



    
