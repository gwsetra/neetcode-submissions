class Solution:
    # top-bottom approach
    def climbStairs(self, n: int) -> int:
        self.cache = [-99] * (n+1)
        print(self.cache)

        def recursive(num):
            if num in (0, 1):
                if self.cache[num] == -99:
                     self.cache[num] = 1
                return self.cache[num] 
            
            # check cache
            if self.cache[num] == -99:
                self.cache[num] = recursive(num-1) + recursive(num-2)
    
            return self.cache[num]
        return recursive(n)