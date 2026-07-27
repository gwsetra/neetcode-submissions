class NumArray:

    def __init__(self, nums: List[int]):
        self.sumcalc = [0]

        for iters in range(1, len(nums)+1):
            # print(iters)
            self.sumcalc.append(self.sumcalc[iters-1] + nums[iters-1])

    def sumRange(self, left: int, right: int) -> int:
        return self.sumcalc[right+1] - self.sumcalc[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)