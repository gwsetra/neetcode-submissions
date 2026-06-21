# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        lists = []
        def backtrack(root, lists):
            if not root:
                print(' inside upper else')
                return False

            lists.append(root.val)
            total = sum(lists)

            print('0----------0')
            print(root.val)
            print(total)
            print(lists)

            # if total > targetSum:
            #     lists.pop()
            #     print('inside melebihi')
            #     print(lists)
            #     return False, lists
            # else:
            if not root.left and not root.right and sum(lists) == targetSum:
                print('kembalikan')
                print(sum(lists))
                return True
            if backtrack(root.left, lists):
                return True
            if backtrack(root.right, lists):
                return True
            lists.pop()
            return False


        return backtrack(root, lists)