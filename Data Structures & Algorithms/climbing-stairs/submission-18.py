class Solution:
    def climbStairs(self, n: int) -> int:
    # space optimised
        cache = {}
        cache[0] = 1
        cache[1] = 1

        print(n, cache)

        for loop in range(2, n+1):
            tmp = cache[0] + cache[1]
            cache[0] = cache[1]
            cache[1] = tmp
        return tmp