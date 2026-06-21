# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.counter = 0
        self.found = None

        def find_small(root, k):
            if not root:
                return None

            find_small(root.left, k)
            self.counter += 1
            if self.counter == k:
                self.found = root.val
            
            find_small(root.right, k)
        
        
        find_small(root, k)
        return self.found