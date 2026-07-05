class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for l in range(32):
            tmp = (n >> l) & 1
            res += (tmp << (31 - l))
            # print(tmp)

        return res