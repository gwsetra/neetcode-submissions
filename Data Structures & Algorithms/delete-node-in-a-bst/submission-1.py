# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def find_min_on_right(root):
            curr = root
            minval = curr.val
            loop = 0
            
            while curr.left:
                curr = curr.left 
                minval = curr.val
                    
                              
            return curr.val 
        
        # print('minimum value')
        # print(find_min(root))

        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else: # current root.val == key
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                minright = find_min_on_right(root.right)
                print('min value on right')
                print(minright)
                root.val = minright
                root.right = self.deleteNode(root.right, minright)
        return root