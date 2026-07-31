# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = 0
        ans = 0
        def order(root):
            nonlocal res
            nonlocal ans
            if not root:
                return
            order(root.left)
            res += 1
            if res == k:
                ans = root.val
                return
            order(root.right)
        order(root)
        return ans