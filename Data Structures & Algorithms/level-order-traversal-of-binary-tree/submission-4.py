# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        lists = deque()
        final = []

        if root:
            lists.append(root)
        
        level = 0
        while len(lists) > 0:
            tmp = []
            for loop in range(len(lists)):
                curr = lists.popleft()
                tmp.append(curr.val)

                if curr.left:
                    lists.append(curr.left)
                if curr.right:
                    lists.append(curr.right)
            final.append(tmp)
            level += 1

        return final