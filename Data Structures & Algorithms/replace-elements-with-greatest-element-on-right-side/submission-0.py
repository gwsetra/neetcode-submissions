class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        idx = None
        biggest = -math.inf
        newarr = []

        for x in range(len(arr)-1, -1, -1):
            if x == len(arr)-1:
                biggest = arr[x]
                newarr = [-1]
                continue
            
            newarr = [biggest] + newarr

            if arr[x] > biggest:
                biggest = arr[x]
        # print(newarr)
        return newarr
            

            
            # print(x)
            # if arr[x] > biggest:
            #     idx = x
            #     biggest = arr[x]
        
        # print(biggest, idx)