class Solution:
    def climbStairs(self, n: int) -> int:
        self.cache = [-99] * (n+1)
        print(self.cache)

        def recursive(num):
            print(num)
            print(self.cache)
            if num in (0, 1):
                print('inside if num')
                print(self.cache[num])
                if self.cache[num] == -99:
                     self.cache[num] = 1
                print(self.cache)
                return self.cache[num] 
            
            # check cache
            if self.cache[num] == -99:
                print('inside -99')
                self.cache[num] = recursive(num-1) + recursive(num-2)
    

            return self.cache[num]
        return recursive(n)