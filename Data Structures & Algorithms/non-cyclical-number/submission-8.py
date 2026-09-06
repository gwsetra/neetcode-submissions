class Solution:
    def isHappy(self, n: int) -> bool:
        def calcsum(x):
            print('inside calcsum')
            # print(x)
            before = x
            res = 0
            while x:
                tmp = x % 10
                # print(tmp)
                if tmp > 0:
                    res += tmp**2
                x = x // 10
            # print(f"{before} become {res}")
            return res

        fast = n
        slow = n
        fast = calcsum(fast)
        print(slow, fast, fast != slow, fast != 1)
        while fast != slow and fast != 1:
            fast = calcsum(fast)
            print(fast)
            fast = calcsum(fast)
            print(fast)
            slow = calcsum(slow)
            print(slow)

        print(slow, fast)
        if fast == 1:
            return True
        if fast == slow:
            return False