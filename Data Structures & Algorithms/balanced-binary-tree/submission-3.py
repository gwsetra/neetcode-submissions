# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return 0
            
            heightleft = dfs(root.left)
            if heightleft == -1:
                return -1

            heightright = dfs(root.right)
            if heightright == -1:
                return -1

            if abs(heightleft - heightright) > 1:
                return -1

            return 1 + max(heightleft, heightright)


        return True if dfs(root) != -1 else False