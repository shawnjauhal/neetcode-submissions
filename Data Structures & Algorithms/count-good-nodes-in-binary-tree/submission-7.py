# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, largest):
            if not node:
                return 0
            res = 1 if node.val >= largest else 0
            largest = node.val if node.val > largest else largest
            return res + dfs(node.left, largest) + dfs(node.right, largest)
        return dfs(root, root.val)