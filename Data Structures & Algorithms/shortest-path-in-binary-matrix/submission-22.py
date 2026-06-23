class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        max_row = len(grid)
        max_col = len(grid[0])
        visited = set()
        queue = deque()
        length = 0
        directions = [[-1, 0], [-1, 1], [0, 1], [1, 1],
                    [1, 0], [1, -1], [0, -1], [-1, -1]]

        visited.add((0,0))
        queue.append((0, 0))

        def bfs(grid):
            nonlocal length
            if (grid[0][0] == 1 or grid[max_row-1][max_col-1] == 1):
                length = -1
                return

            while len(queue):
                # print(queue)
                # if (max_row - 1, max_col - 1) in queue:
                #     # print('reached destination')
                #     length += 1
                #     return 
                for loop in range(len(queue)):
                    c_row, c_col = queue.popleft()
                    
                    if (c_row, c_col) == (max_row - 1, max_col - 1):
                        length += 1
                        # print('reached destination')
                        return

                    for dr, dc in directions:
                        if (min(c_row+dr, c_col+dc) < 0 or
                        c_row+dr == max_row or c_col+dc == max_col or
                        grid[c_row+dr][c_col+dc] == 1 or
                        (c_row+dr, c_col+dc) in visited):
                            continue
                        
                        
                        # visited.add((c_row+dr, c_col+dc))
                        grid[c_row+dr][c_col+dc] =1
                        queue.append((c_row+dr, c_col+dc))

                length += 1
            length = -1
        
        bfs(grid)
    
        return length