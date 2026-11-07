# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res =0 

        def dfs(val, node):
            nonlocal res
            if not node:
                return
            if node.val >= val:
                res += 1
            dfs(max(val, node.val), node.left)
            dfs(max(val, node.val), node.right)
        dfs(float('-inf'), root)
        return res

    