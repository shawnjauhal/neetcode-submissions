# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque()
        q.append(root)

        while q:
            qLen = len(q)
            right = True
            for i in range(qLen):
                node = q.popleft()
                if node:
                    if right:
                        res.append(node.val)
                        right = False
                    q.append(node.right)
                    q.append(node.left)
        return res