class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ori_value = image[sr][sc]
        def dfs(image, curr_row, curr_col, color):

            if (min(curr_row, curr_col) < 0 
                or (curr_row == len(image)) or curr_col == len(image[0])
                or image[curr_row][curr_col] != ori_value):

                return
            image[curr_row][curr_col] = color

            dfs(image, curr_row-1, curr_col, color) # atas
            dfs(image, curr_row, curr_col+1, color) # kanan
            dfs(image, curr_row+1, curr_col, color) # bawah
            dfs(image, curr_row, curr_col-1, color) # bawah


        if image[sr][sc] == color:
            return image
        dfs(image, sr, sc, color)

        return image    
