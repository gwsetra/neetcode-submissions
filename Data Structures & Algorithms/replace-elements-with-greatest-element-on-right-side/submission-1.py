class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        idx = None
        biggest = -math.inf
        newarr = []

        for x in range(len(arr)-1, -1, -1):
            print(x, arr, biggest)
            tmp = arr[x]
            if x == len(arr)-1:
                biggest = arr[x]
                arr[x] = -1
                continue
            
            # newarr = [biggest] + newarr
            arr[x] = biggest

            if tmp > biggest:
                biggest = tmp
        # print(newarr)
        return arr
            

            
            # print(x)
            # if arr[x] > biggest:
            #     idx = x
            #     biggest = arr[x]
        
        # print(biggest, idx)