# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # Base case: if the node is empty, there is no path
        if not root:
            return False

        # If it's a leaf node, check if its value matches the remaining target sum
        if not root.left and not root.right:
            return root.val == targetSum

        # Recurse down to children, subtracting the current node's value from the target
        remaining_sum = targetSum - root.val

        # Short-circuit: if the left subtree finds the path, the right subtree is never evaluated
        return self.hasPathSum(root.left, remaining_sum) or self.hasPathSum(
            root.right, remaining_sum
        )