class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        lenturb = 0
        cur = 0
        lastop = None
        l = 0

        if len(arr) == 1:
            return 1
        
        r = 1

        for r in range(1, len(arr)):
            print('***')
            print(arr[r], arr[cur], arr[l], lastop)
            if lastop is None:
                if arr[r] < arr[cur]:
                    lastop = '-'
                elif arr[r] > arr[cur]:
                    lastop = '+'
                else:
                    l=r
            elif (arr[r] < arr[cur] and lastop == '-') or (arr[r] > arr[cur] and lastop == '+'):
                print('inside if')
                lenturb = max(lenturb, r-l)
                l=r
            elif arr[r] == arr[cur]:
                print('inside else')
                lenturb = max(lenturb, r-l+1)
                l=r
            else:
                if arr[r] < arr[cur]:
                    lastop = '-'
                else:
                    lastop = '+'
            lenturb = max(lenturb, r-l+1)
            cur = r
        print(lenturb)
        return lenturb

        