class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l=0
        avg = 0
        sets = []
        counter = 0

        for idx in range(len(arr)):
            if idx-l >= k:
                sets.pop(0)
            sets.append(arr[idx])
            # print(sets)
            # print(sum(sets)/k)
            if len(sets) == k and sum(sets)/k >= threshold:
                print('yess')
                counter += 1
        return counter