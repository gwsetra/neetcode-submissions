class Solution:
    def mySqrt(self, x: int) -> int:
        lower = 0
        upper = x
        mid = x // 2

        while lower < upper:
            midsqr = mid*mid
            print(lower, mid, upper)
            print(midsqr, x)
            if midsqr == x:
                return mid
            if midsqr > x:
                upper = mid - 1
            if midsqr < x:
                lower = mid + 1
            mid = lower + ((upper-lower) // 2)
            print(lower, mid, upper)
        return lower