class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        counter = 0
        for loop1 in range(len(grid)):
            for loop2 in range(len(grid[0])):
                print(loop1, loop2)
                print(grid[loop1][loop2])
                print(grid[loop1][loop2] == 1)
                if grid[loop1][loop2] == '1':
                    counter += 1+ self.dfs(grid, loop1, loop2)
                    print('finished asoy')
        return counter
    
    def dfs(self, grid, row, column):
        print('inside dfs :', row, column)
        print('grid', grid)
        if ((min(row, column) < 0)
        or row == len(grid) or column == len(grid[0]) or
        grid[row][column] == '0'):
            print('unwanted place')
            return

        grid[row][column] = '0'

        self.dfs(grid, row-1, column) # atas
        self.dfs(grid, row, column +1) # kanan
        self.dfs(grid, row+1, column) # bawah
        self.dfs(grid, row, column-1) # kiri

        print('end')

        return 0


    
