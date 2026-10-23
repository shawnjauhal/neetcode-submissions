# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, largest, curr=0):
            res = curr
            if root.val >= largest:
                res += 1
                largest = root.val
            if root.left:
                res += dfs(root.left, largest, curr)
            if root.right:
                res += dfs(root.right, largest, curr)
            return res
        return dfs(root, root.val)