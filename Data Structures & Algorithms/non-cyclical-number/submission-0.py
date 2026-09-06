class Solution:
    def isHappy(self, n: int) -> bool:
        maps = set()
        sum = n
        loop = 0

        while sum not in maps and sum != 1 and loop < 100:
            tmp = 0
            for i in range(len(str(sum))):
                # print(str(n)[i])
                tmp += int(str(n)[i])**2
            if tmp not in maps:
                maps.add(tmp)
            print(tmp)
            sum = tmp
            loop += 1
        
        if sum == 1:
            return True
        if sum in maps:
            return False
        return True