"""
# Definition for a Node.
class Node:, clear_overloads
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        cloneMap = {}
        
        def dfs(node):
            if not node:
                return None
                
            if node in cloneMap:
                return cloneMap[node]
            copy = Node(node.val)
            cloneMap[node]=copy
            for nei in node.neighbors:
                nei_clone = dfs(nei)
                copy.neighbors.append(nei_clone)
            return copy
        
        return dfs(node)