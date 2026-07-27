class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = [[0] for _ in range(len(matrix))]
        # self.matrix[0].append(1)
        # print(self.matrix)

        # attach 0 to matrix
        for iterx, item in enumerate(matrix):
            for itery in range(1, len(item)+1):
                # print(num)
                # print(iterx, itery)

                self.matrix[iterx].append(self.matrix[iterx][itery-1] + item[itery-1])
        # print(self.matrix)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # print(f'sumRegion {row1}, {col1}, {row2}, {col2}')
        tmp = 0
        for iterx in range(row1, row2+1):
            # print(iterx, col1, iterx, col2)
            # print(self.matrix[iterx][col2+1], self.matrix[iterx][col1])
            tmp += self.matrix[iterx][col2+1] - self.matrix[iterx][col1]
        return tmp


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)