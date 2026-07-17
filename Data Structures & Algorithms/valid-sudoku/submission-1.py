class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cacherow = defaultdict(list)
        cachecol = defaultdict(list)
        row = len(board)
        col = len(board[0])

        def checksubmatrix(startrow, startcol, board):
            smallcache = defaultdict(list)
            # print('inside checksubmatrix', startrow, startcol)
            for itemx in range(startrow, startrow+3, 1):
                # print('--**--')
                for itemy in range(startcol, startcol+3, 1):
                    # print(itemx, itemy)
                    if board[itemx][itemy] != '.':
                        if board[itemx][itemy] not in cacherow[itemx]:
                            cacherow[itemx].append(board[itemx][itemy])
                        else:
                            # print('duplicate found in cacherow')
                            return False
                        if board[itemx][itemy] not in cachecol[itemy]:
                            cachecol[itemy].append(board[itemx][itemy])
                        else:
                            # print('duplicate found in cachecol')
                            return False
                        
                        if board[itemx][itemy] not in smallcache[(startrow, startcol)]:
                            smallcache[(startrow, startcol)].append(board[itemx][itemy])
                        else:
                            # print('duplicate found in 3x3 matrix')
                            return False
                        
                    # print(cacherow, cachecol)
                    # print(smallcache)
            return True

        for rowloop in range(0, col, 3):
            for colloop in range(0, row, 3):
                # print(rowloop, colloop)
                res = checksubmatrix(rowloop, colloop, board)
                if not res:
                    return False
                # if board[rowloop][colloop] != '.':
                #     print('found number')
                #     cache[(rowloop, colloop)] = board[rowloop][colloop]
        return True
        # print(cache)



