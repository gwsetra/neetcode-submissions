class Solution:
    def climbStairs(self, n: int) -> int:
    # space optimised
        cache = {}
        cache[0] = 1
        cache[1] = 1
        tmp = 0

        for loop in range(2, n+1):
            tmp = cache[0] + cache[1]
            cache[0] = cache[1]
            cache[1] = tmp
        return 1 if not tmp else tmp