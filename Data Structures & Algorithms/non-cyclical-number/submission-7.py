class Solution:
    def isHappy(self, n: int) -> bool:
        maps = set()
        sum = n
        loop = 0

        while sum not in maps and  sum != 1:
            maps.add(sum)
            tmp = 0
            for i in range(len(str(sum))):
                tmp += int(str(sum)[i])**2
            sum = tmp
        
        if sum == 1:
            return True
        if sum in maps:
            return False
        return True