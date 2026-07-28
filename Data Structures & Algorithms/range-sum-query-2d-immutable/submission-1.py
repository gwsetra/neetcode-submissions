class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.summatrix = [[0 for _ in range(len(matrix)+1)] for _ in range(len(matrix[0])+1)]
        print(self.summatrix)

        for iterx in range(1, len(matrix)+1):
            # print(iterx)
            for itery in range(1, len(matrix[0])+1):
                # print(itery)
                self.summatrix[iterx][itery] = self.summatrix[iterx-1][itery] + self.summatrix[iterx][itery-1] + matrix[iterx-1][itery-1] - self.summatrix[iterx-1][itery-1]  
        print(self.summatrix)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        print(f'sumRegion {row1}, {col1}, {row2}, {col2}')
        print(self.summatrix[row2+1][col2+1], self.summatrix[(row2+1)][(col2+1)-(col1+1)], self.summatrix[(row2+1)-(row1+1)][(col2+1)], self.summatrix[row1][col1])
        return self.summatrix[row2+1][col2+1] - self.summatrix[(row2+1)][col1] - self.summatrix[row1][(col2+1)] + self.summatrix[row1][col1] 


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)