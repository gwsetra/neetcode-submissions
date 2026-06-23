from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        max_row = len(grid)
        max_col = len(grid[0])
        visited = set()
        queue = deque()
        queue.append((0, 0))
        visited.add((0, 0))
        length = 0

        def bfs():
            nonlocal length
            direction = [[1, 1], [0, 1], [1, 0], [-1, 0], 
                    [-1, 1], [1, -1],[0, -1], [-1, -1]]
            
            if grid[0][0] == 1:
                return -1
            
            while len(queue):
                # row, column = queue.popleft()
                row, column = max(queue)
                length += 1


                for dr, dc in direction:
                    # print('current row, column = ', row, column)

                    if (max_row-1, max_col-1) in visited:
                        # print('sudah sampai visited')
                        length += 1
                        return length

                    if (min(row+dr, column+dc) < 0 or 
                    row+dr == max_row or column+dc == max_col or
                    grid[row+dr][column+dc] == 1 or
                    (row+dr, column+dc) in visited):
                        continue
                    
                    

                    
                    queue.append((row+dr, column+dc))
                    visited.add((row+dr, column+dc))

                    # print('row, column when adding = ', row+dr, column+dc)
                    # print('add length', length)
                    # print('visited', visited)
                    
                    # print('new length', length)
        
        return bfs()