# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')

        def helper(root, sum, inc):
            nonlocal res
            if not root:
                return 0
            res = max(res, root.val)
            if not inc:
                helper(root.left, 0, False)
                helper(root.right, 0, False)
                val = max(0,helper(root.left, 0, True)) + helper(root.right, 0, True) + root.val
                res = max(val, res)
            else:
                return root.val + max(0, helper(root.left, sum, True), helper(root.right, sum, True))


        helper(root, 0, False)
        return res
        