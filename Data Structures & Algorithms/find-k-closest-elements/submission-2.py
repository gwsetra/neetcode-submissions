class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        lp = 0
        lenarr = len(arr)-1
        rp = lenarr
        loop = 0
        res = []
        cnt = 0

        while lp < rp and loop < 10:
            mid = ((rp-lp) // 2) + lp
            print(lp, mid, rp)

            if mid == x:
                print('mid x')
                break
            elif mid < x:
                print('geser kanan')
                lp = mid+1
            elif x < mid:
                print('geser kiri')
                rp = mid
            loop += 1

        res.append(arr[mid])
        cnt += 1

        print(lp, mid, rp)

        lp = mid - 1
        rp = mid + 1
        while cnt < k:
            # if on extreme left
            if mid == 0:
                print('mid is on extreme left')
                res.extend(arr[mid+1:(mid+1)+k-cnt])
                break
            # if on extreme right
            if mid == lenarr:
                print('mid is on extreme right')
                res.extend(arr[mid-(k-cnt):mid])
                break
            # else
            else:
                print('mid is in between')

                if arr[rp]-arr[mid] < arr[lp]-arr[mid]:
                    print('append right')
                    res.append(arr[rp])
                    rp += 1
                    cnt += 1

                elif (arr[lp]-arr[mid] < arr[rp]-arr[mid]) or arr[lp]-arr[mid] == arr[rp]-arr[mid]:
                    print('append left')
                    res.append(arr[lp])
                    lp -= 1
                    cnt += 1

        print(res)
        res.sort()            
        return res