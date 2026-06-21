class Solution:
    memo = []
    def climbStairs(self, n: int) -> int:
        if len(self.memo) == 0 and n in (0,1):
            self.memo.append(1)
            self.memo.append(1)
            return 1
        elif len(self.memo) > 0 and n in (0,1):
            return self.memo[n]
        else:
            val1 = self.climbStairs(n-1)
            val2 = self.climbStairs(n-2)
            if n > len(self.memo):
                self.memo.append(val1+val2)
            return val1 + val2