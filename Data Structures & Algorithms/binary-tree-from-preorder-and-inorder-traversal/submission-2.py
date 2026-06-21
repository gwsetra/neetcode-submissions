# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def buildthetree(preorder, inorder):
            if not preorder or not inorder:
                return None

            root = TreeNode(preorder[0])
            mid = None

            # find element location where match root from inorder
            for asdf in range(len(inorder)):
                if inorder[asdf] == root.val:
                    mid = asdf
                    break

            root.left = buildthetree(preorder[1 : mid+1], inorder[:mid])
            root.right = buildthetree(preorder[mid+1 :], inorder[mid+1:])

            return root
        return buildthetree(preorder, inorder)