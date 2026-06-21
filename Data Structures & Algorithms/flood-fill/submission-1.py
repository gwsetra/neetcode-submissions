class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # print(image)
        # print(sr, sc)
        ori_value = image[sr][sc]
        def dfs(image, curr_row, curr_col, color):
            print('current position', curr_row, curr_col)
            if (min(curr_row, curr_col) < 0 
                or (curr_row == len(image)) or curr_col == len(image[0])
                or image[curr_row][curr_col] != ori_value
                or image[curr_row][curr_col] == color):
                print(min(curr_row, curr_col) < 0 , (curr_row == len(image[0])), curr_col == len(image))
                print('return')
                return
            elif image[curr_row][curr_col] == ori_value:
                print('continue process, update value')
                print('current image', image)
                image[curr_row][curr_col] = color
                print('after updated image', image)

                dfs(image, curr_row-1, curr_col, color) # atas
                dfs(image, curr_row, curr_col+1, color) # kanan
                dfs(image, curr_row+1, curr_col, color) # bawah
                dfs(image, curr_row, curr_col-1, color) # bawah


        dfs(image, sr, sc, color)

        return image    
        