# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float("-inf")
        def dfs(root):
            nonlocal res
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)

            res = max(res,root.val,root.val + left, root.val + right, root.val + left + right)
            temp = 0 if max(right, left) <= 0 else max(right, left)
            return root.val + temp
        dfs(root)
        return res