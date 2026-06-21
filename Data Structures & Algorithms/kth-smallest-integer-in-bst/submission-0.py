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
            print('-----')
            print(root.val)
            print(self.counter)

            find_small(root.left, k)
            self.counter += 1
            if self.counter == k:
                print('inside if')
                print(self.counter)
                print(root.val)
                self.found = root.val
                # return root.val
            
            # print(root.val)
            # print('counter :', self.counter)
            
            find_small(root.right, k)
        
        
        print(find_small(root, k))
        print('1231231')
        return self.found