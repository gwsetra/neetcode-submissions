class Solution:
    def mySqrt(self, x: int) -> int:
        lower = 0
        upper = x
        mid = x // 2
        tmpval = None
        ans = None

        while lower <= upper:
            mid = lower + ((upper-lower) // 2)
            midsqr = mid*mid
            print(lower, mid, upper)
            print(midsqr, x)
            if midsqr == x:
                return mid
            if midsqr > x:
                upper = mid - 1
            if midsqr < x:
                print('increase lower')
                ans = mid
                lower = mid + 1
            print(lower, mid, upper)
        return ans