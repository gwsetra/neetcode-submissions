class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ori_value = image[sr][sc]
        def dfs(curr_row, curr_col):
            if (min(curr_row, curr_col) < 0 
                or (curr_row == len(image)) or curr_col == len(image[0])
                or image[curr_row][curr_col] != ori_value):

                return
            image[curr_row][curr_col] = color

            dfs(curr_row-1, curr_col) # atas
            dfs( curr_row, curr_col+1) # kanan
            dfs( curr_row+1, curr_col) # bawah
            dfs(curr_row, curr_col-1) # bawah


        if image[sr][sc] == color:
            return image
        dfs(sr, sc)

        return image    
