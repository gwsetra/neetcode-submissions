memo = []

class Solution:
    def climbStairs(self, n: int) -> int:
        if n > 30:
            return 0
        if len(memo) == 0 and n in (0,1):
            memo.append(1)
            memo.append(1)
            return 1
        elif len(memo) > 0 and n in (0,1):
            return memo[n]
        else:
            val1 = self.climbStairs(n-1)
            val2 = self.climbStairs(n-2)
            if n > len(memo):
                memo.append(val1+val2)
            return val1 + val2