"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        loop = 0
        copied = {}
        result = defaultdict(list)
        result2 = []

        def dfs(node):
            if not node:
                return None
                
            if node in copied:
                return copied[node]
            nnode = Node(node.val)
            copied[node] = nnode

            print(nnode)
            print(copied)

            for nextnode in node.neighbors:
                nnode.neighbors.append(dfs(nextnode))
            return nnode


        
        return dfs(node)
