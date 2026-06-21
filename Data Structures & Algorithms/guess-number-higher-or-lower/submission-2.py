# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        minval = 1
        maxval = n
        middle = (minval+maxval) // 2
        print(minval, middle, maxval)
        loop =0

        while loop < 10:
            middle = (minval+maxval) // 2
            print(minval, middle, maxval)
            print(guess(middle))
            if guess(middle) == 0:
                return middle
            elif guess(middle) == -1:
                maxval = middle + 1
            elif guess(middle) == 1:
                minval = middle - 1
            loop += 1
