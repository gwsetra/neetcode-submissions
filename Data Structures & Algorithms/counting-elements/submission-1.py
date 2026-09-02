class Solution:
    def countElements(self, arr: List[int]) -> int:
        counter = 0
        print(list(set(arr)))
        for i in range(len(list(set(arr)))-1):
            if arr[i]+1 == arr[i+1]:
                counter += 1
        return counter