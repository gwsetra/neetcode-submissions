class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l=0
        avg = 0
        currentsum = 0
        counter = 0
        lencounter = 0

        for idx in range(len(arr)):
            if idx-l >= k:
                if lencounter > 1:
                    # print('prev avg', avg)
                    # print(avg * (lencounter)- sets[0])
                    avg = ((avg * (lencounter)) - arr[l]) / (lencounter-1)
                    # print('new avg', avg)
                # sets.pop(0)
                currentsum -= arr[l]
                l+= 1
                lencounter -= 1

            currentsum += arr[idx]
            lencounter += 1
            # print(sets)
            # print(sum(sets)/k)
            if lencounter == 1:
                avg = arr[idx]
            else:
                # print('==>',avg ,(lencounter-1), arr[idx],lencounter)
                avg = ((avg * (lencounter-1)) + arr[idx]) / lencounter
            # print('avg', avg)
            if avg >= threshold and lencounter == k:
                # print('yess')
                counter += 1
        return counter