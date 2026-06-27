class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        max_row = len(grid)
        max_col = len(grid[0])
        fresh_checker = set()
        visited = set()
        queue = deque()
        num_of_minutes = -1 
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

        def bfs():
            nonlocal num_of_minutes

            # print('start bfs')


            while len(queue):
                # print('content of queue', queue)
                for loop in range(len(queue)):
                    r, c = queue.popleft()

                    for dr, dc in directions:

                        if (min(r+dr, c+dc) < 0 or
                        r+dr == max_row or c+dc == max_col 
                        or grid[r+dr][c+dc] == 0 or
                        (r+dr, c+dc) in visited ):
                            continue

                        if grid[r+dr][c+dc] == 1:
                            queue.append((r+dr, c+dc))
                            visited.add((r+dr, c+dc))

                num_of_minutes += 1
                    
        
        for loopr in range(max_row):
            for loopc in range(max_col):
                if grid[loopr][loopc] == 1:
                    fresh_checker.add((loopr, loopc))
                if grid[loopr][loopc] == 2:
                    # print('rotten found', loopr, loopc)
                    # bfs(loopr, loopc)
                    queue.append((loopr, loopc))
                    visited.add((loopr, loopc))
        
        bfs()
        # print(fresh_checker)
        # print(visited)

        if len(fresh_checker) == 0: # if there's no 1 or fresh fruite
            return 0
        else:
            return num_of_minutes if fresh_checker.issubset(visited)  else -1

                    
