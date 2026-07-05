class Solution:
    def countBits(self, n: int) -> List[int]:
        # using dynammic programming 
        cache = {0: 0, 1:1}
        result = []
        def countone(n):
            # print(n)

            if n in cache:
                result.append(cache[n])
                return
            
            bitform = format(n, 'b')
            bitremainlen = (bitform[1:])
            # print(bitform, bitremainlen)
            # print(int(bitremainlen, 2))
            # print(cache[int(bitremainlen, 2)])
            # print('one count')
            # print(1 + cache[int(bitremainlen)])
            cache[n] = 1 + cache[int(bitremainlen, 2)]
            result.append(1 + cache[int(bitremainlen, 2)])
            
        
        # countone(2)
        # countone(3)

        # countone(15)
        for loop in range(n+1):
            countone(loop)
        
        return result

