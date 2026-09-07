# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Codec:
    # Encodes using BFS while-loop
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        
        queue = deque([root])
        res = []
        
        while len(queue) != 0:
            node = queue.popleft()
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append("#")
                
        return ",".join(res)

    # Decodes using BFS while-loop
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        
        values = deque(data.split(","))
        root_val = values.popleft()
        if root_val == "#":
            return None
            
        root = TreeNode(int(root_val))
        queue = deque([root])
        
        while len(queue) != 0:
            parent = queue.popleft()
            
            # Left child
            if values:
                left_val = values.popleft()
                if left_val != "#":
                    parent.left = TreeNode(int(left_val))
                    queue.append(parent.left)
            
            # Right child
            if values:
                right_val = values.popleft()
                if right_val != "#":
                    parent.right = TreeNode(int(right_val))
                    queue.append(parent.right)
                    
        return root