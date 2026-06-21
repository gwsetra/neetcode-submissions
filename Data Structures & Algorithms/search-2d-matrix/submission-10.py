import math
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)-1
        n = len(matrix[0])-1
        
        if target < matrix[0][0] or target > matrix[m][n]:
            return False
        elif target == matrix[0][0]:
            return True
        
        mleft = 0
        mright = m
        mmiddle = math.floor((0+m)/2)


        while mleft <= mright:
            mmiddle = math.floor((mleft+mright)/2)
            if matrix[mmiddle][0] == target:
                return True
            elif matrix[mmiddle][0] < target:
                mleft = mmiddle + 1
            elif matrix[mmiddle][0] > target:
                mright = mmiddle -1

        if target < matrix[mmiddle][0]:
            mmiddle = mmiddle-1
   
        nleft = 0
        nright = n
        nmiddle = math.floor((nleft+nright)/2)

        while nleft <= nright:
            nmiddle = math.floor((nleft+nright)/2)

            if matrix[mmiddle][nmiddle] == target:
                return True
            elif matrix[mmiddle][nmiddle] < target:
                nleft = nmiddle + 1
            elif matrix[mmiddle][nmiddle] > target:
                nright = nmiddle -1
        return False