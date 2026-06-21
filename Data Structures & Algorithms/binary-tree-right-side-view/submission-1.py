# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        lists = deque()
        final = []
        max_per_level = 0

        if root:
            lists.append(root)

        level = 0
        while len(lists)>0:
            max_per_level = len(lists)-1
            for iter in range(0, len(lists)):
                curr = lists.popleft()

                print(iter, max_per_level)
                if iter == max_per_level:
                    final.append(curr.val)

                if curr.left:
                    lists.append(curr.left)
                if curr.right:
                    lists.append(curr.right)
            level +=1
        return final