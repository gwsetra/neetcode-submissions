class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        sums = 0
        cache[1] = 1
        cache[2] = 2

        def memo(n):
            nonlocal sums
            # print('current memo n,', n)
            if n==0:
                return 0

            if n in cache:
                # print('value in cache')
                return cache[n]

            sums += memo(n-1) + memo(n-2)
            if n not in cache:
                # print('adding new cache n, sum',n, sums)
                cache[n] = sums
            return sums
        
        return memo(n)

            
        
