class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 0 or n > 30:
            return False
        elif n in (0,1):
            return 1
        else:
            return self.climbStairs(n-1) + self.climbStairs(n-2)