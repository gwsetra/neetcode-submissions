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
                print('inside if not root')
                return 0
            print(root.val)
            
            heightleft = dfs(root.left)
            heightright = dfs(root.right)
            if heightleft == -1 or heightright == -1:
                return -1
            elif abs(heightleft - heightright) <= 1:
                current_height = 1 + max(heightleft, heightright)
            else:
                return -1
            
            if root.left is None and root.right is None:
                print('inside if')
                print('my current val is', root.val)
                print('my current height is ', current_height)
                return 1
            else:
                print('inside else')
                print('my current val is', root.val)
                print('my current height is ', current_height)
                print('my left height is', heightleft)
                print('my right height is', heightright)
                return current_height

        return True if dfs(root) != -1 else False