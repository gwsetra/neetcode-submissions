class Solution:
    def countElements(self, arr: List[int]) -> int:
        counter = 0
        tmp = list(set(arr))
        # print(tmp)
        for i in range(len(list(set(arr)))-1):
            # print(tmp[i], tmp[i]+1, tmp[i+1])
            if tmp[i]+1 == tmp[i+1]:
                counter += 1
        return counter