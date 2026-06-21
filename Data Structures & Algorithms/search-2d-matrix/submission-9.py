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


        while mleft <= mright:
            print('loop 1st')
            mmiddle = math.floor((mleft+mright)/2)
            print(mleft, mmiddle, mright)
            print(matrix[mmiddle][0], target)
            if matrix[mmiddle][0] == target:
                print('found')
                return True
            elif matrix[mmiddle][0] < target:
                print('a')
                mleft = mmiddle + 1
            elif matrix[mmiddle][0] > target:
                print('b')
                mright = mmiddle -1

        if target < matrix[mmiddle][0]:
            mmiddle = mmiddle-1

        print(mleft, mmiddle, mright)    
        nleft = 0
        nright = n
        nmiddle = math.floor((nleft+nright)/2)
        print('second iter')
        print(nleft, nmiddle, nright)
        while nleft <= nright:
            nmiddle = math.floor((nleft+nright)/2)
            print(nleft, nmiddle, nright)
            print(matrix[mmiddle][nmiddle], target)
            if matrix[mmiddle][nmiddle] == target:
                return True
            elif matrix[mmiddle][nmiddle] < target:
                print('here')
                nleft = nmiddle + 1
                print(nleft, nmiddle, nright)
            elif matrix[mmiddle][nmiddle] > target:
                print('there')
                nright = nmiddle -1
        return False