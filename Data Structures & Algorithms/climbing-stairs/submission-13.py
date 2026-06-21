

class Solution:
    def __init__(self):
        self.memo = []

    def climbStairs(self, n: int) -> int:
        # print('loop number :', n)
        if len(self.memo) == 0 and n in (0,1):
            self.memo.append(1)
            self.memo.append(1)
            return 1
        elif len(self.memo) > 0 and n in (0,1):
            return self.memo[n]
        else:
            if n-1 > len(self.memo):
                val1 = self.climbStairs(n-1)
            else:
                val1 = self.memo[n-1]

            if n-2 > len(self.memo):
                val2 = self.climbStairs(n-2)
            else:
                val2 = self.memo[n-2]
            self.memo.append(val1+val2)
            return val1 + val2