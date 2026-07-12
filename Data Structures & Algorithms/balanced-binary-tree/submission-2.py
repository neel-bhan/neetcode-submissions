# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = False
        def helper(root):  
            nonlocal res
            if not root:
                return 0
            left, right = helper(root.left), helper(root.right) 
            if not res:
                res = True if(abs(left - right) > 1) else False
            return 1 + max(left, right)
        helper(root)
        return not res

        