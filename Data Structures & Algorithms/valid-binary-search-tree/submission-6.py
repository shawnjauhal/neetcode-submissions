# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, minL, maxR):
            if not node:
                return True
            if node.val <= minL or node.val >= maxR:
                return False
            return dfs(node.left, minL, node.val) and dfs(node.right, node.val, maxR)
        return dfs(root, -math.inf, math.inf)
        