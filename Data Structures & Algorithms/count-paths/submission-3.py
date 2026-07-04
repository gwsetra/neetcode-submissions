class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # print(m, n)
        prev = [0]*n
        
        # print(prev, curr)

        for lx in range(m-1, -1, -1):
            # print(lx)
            curr = [0]*n
            curr[n-1] = 1
            
            for ly in range(n-2, -1, -1):
                # print(lx, ly)
                # print('neighbors, right, bottom', curr[ly+1], prev[ly])
                curr[ly] = curr[ly+1] + prev[ly]
            # print('final curr', curr)
            prev = curr
        
        return curr[0]