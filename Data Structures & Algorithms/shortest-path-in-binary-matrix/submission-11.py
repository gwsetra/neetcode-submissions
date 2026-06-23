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
        shorter_row = 0
        shorter_column = 0

        def bfs():
            nonlocal length, shorter_row, shorter_column
            direction = [[1, 1], [0, 1], [1, 0], [-1, 0], 
                    [-1, 1], [1, -1],[0, -1], [-1, -1]]
            
            if grid[0][0] == 1:
                return -1
            
            while len(queue):
                # 
                # row, column = max(queue)
                # queue.clear()
                
                maxs = 0
                shorter_path = ()
                print('finding shorter path')
                for loop2 in range(len(queue)):
                    row, column = queue.popleft()
                    print(row, column, maxs)
                    if row+column >= maxs:
                        shorter_row, shorter_column = row, column
                        maxs = row+column
                print('shorter path', shorter_row, shorter_column)
                length += 1


                for dr, dc in direction:
                    # print('current row, column = ', row, column)

                    if (max_row-1, max_col-1) in visited:
                        print(visited)
                        print('sudah sampai visited')
                        length += 1
                        return length

                    if (min(shorter_row+dr, shorter_column+dc) < 0 or 
                    shorter_row+dr == max_row or shorter_column+dc == max_col or
                    grid[shorter_row+dr][shorter_column+dc] == 1 or
                    (shorter_row+dr, shorter_column+dc) in visited):
                        continue
                                 
                    queue.append((shorter_row+dr, shorter_column+dc))
                    visited.add((shorter_row+dr, shorter_column+dc))
                
            return -1

        return bfs()