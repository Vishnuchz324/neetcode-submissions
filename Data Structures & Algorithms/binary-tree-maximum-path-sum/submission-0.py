# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = [float('-inf')]
        self.calculate_branch_sum(root,max_sum)
        return max_sum[0];

    def calculate_branch_sum(self,root:Optional[TreeNode],max_sum:int)->int:
        if root is None:
            return 0
        ls = max(0,self.calculate_branch_sum(root.left,max_sum))
        rs = max(0,self.calculate_branch_sum(root.right,max_sum))
        max_sum[0] = max(max_sum[0],root.val + ls + rs)
        return root.val+max(ls,rs)