class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0, 1]
        for l in range(2, n+1):
            counter = 0
            tmp = l
            while tmp > 0:
                # print('inside tmp')
                if tmp & 1 == 1:
                    counter += 1
                tmp = tmp >> 1
            result.append(counter)
        return result