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
            heightright = dfs(root.right)
            if heightleft == -1 or heightright == -1:
                return -1
            elif abs(heightleft - heightright) <= 1:
                current_height = 1 + max(heightleft, heightright)
            else:
                return -1
            
            if root.left is None and root.right is None:
                return 1
            else:
                return current_height

        return True if dfs(root) != -1 else False