class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l=0
        currentsum = 0
        counter = 0
        lencounter = 0

        for idx in range(len(arr)):
            if idx-l >= k:
                currentsum -= arr[l]
                l+= 1
                lencounter -= 1

            currentsum += arr[idx]
            lencounter += 1
            # print(sets)
            # print(sum(sets)/k)
            # print('currentsum', currentsum)
            if currentsum >= threshold * k and lencounter == k:
                # print('yess')
                counter += 1
        return counter