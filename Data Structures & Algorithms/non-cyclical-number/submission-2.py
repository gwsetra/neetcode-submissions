class Solution:
    def isHappy(self, n: int) -> bool:
        maps = set()
        sum = n
        loop = 0

        while  sum != 1:
            # print('***')
            # print(sum)
            tmp = 0
            for i in range(len(str(sum))):
                # print(str(sum)[i])
                tmp += int(str(sum)[i])**2
            if tmp not in maps:
                maps.add(tmp)
            else:
                return False
            # print('tmp',tmp)
            sum = tmp
            # print(sum not in maps)
        
        if sum == 1:
            return True
        if sum in maps:
            return False
        return True