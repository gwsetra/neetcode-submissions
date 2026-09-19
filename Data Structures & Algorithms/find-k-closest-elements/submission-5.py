class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        lp = 0
        lenarr = len(arr)-1
        rp = lenarr

        while lp < rp and rp-lp > k-1:
            # print(lp, rp)
            diffleft = abs(arr[lp]-x)
            diffright = abs(arr[rp]-x)
            # print(diffleft, diffright)

            if diffright < diffleft:
                # print('shift left')
                lp += 1
            else:
                # print('shift right')
                rp -= 1
        # print(lp, rp)
        return arr[lp:rp+1]

