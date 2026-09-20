class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # let compute modified binary search show in video
        lp = 0
        rp = len(arr)-k # last index in arr where window fit k
        loop = 0
        mid = ((rp-lp) // 2) + lp

        while lp < rp :
            # print(abs(x-arr[mid+(k)]), abs(x-arr[mid]))
            if abs(x-arr[mid]) < abs(x-arr[mid+(k)]) or (abs(x-arr[mid]) == abs(x-arr[mid+(k)]) and arr[mid] < arr[mid+(k)]):
                rp = mid
            else:
                lp = mid + 1
            mid = ((rp-lp) // 2) + lp

        return arr[mid:mid+k]