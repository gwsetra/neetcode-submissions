import math
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)-1
        n = len(matrix[0])-1
        print(m, n)
        
        if target < matrix[0][0] or target > matrix[m][n]:
            return False
        elif target == matrix[0][0]:
            return True
        
        mleft = 0
        mright = m
        mmiddle = math.floor((0+m)/2)
        print('1')
        print(mleft, mright)


        while mleft < mright:
            mmiddle = math.floor((0+m)/2)
            print(mleft, mmiddle, mright)
            if matrix[mmiddle][0] == target:
                return True
            elif matrix[mmiddle][0] < target:
                mleft = mmiddle + 1
            elif matrix[mmiddle][0] > target:
                mright = mmiddle -1

        if target < matrix[mmiddle][0]:
            mmiddle = mmiddle-1

        print(mleft, mmiddle, mright)    
        nleft = 0
        nright = n
        loop = 1
        print('second iter')
        while nleft < nright:
            nmiddle = math.floor((nleft+n)/2)
            print(nleft, nmiddle, nright)
            if matrix[mmiddle][nmiddle] == target:
                return True
            elif matrix[mmiddle][nmiddle] < target:
                nleft = nmiddle + 1
            elif matrix[mmiddle][nmiddle] > target:
                nright = nmiddle -1
            loop +=1
        return False