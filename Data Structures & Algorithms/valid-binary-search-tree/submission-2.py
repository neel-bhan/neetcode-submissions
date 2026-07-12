# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        min, max = float("-inf"), float("inf")

        def valid(root, min, max):
            if not root:
                return True
            if root.val > min and root.val < max:
                return valid(root.right, root.val, max) and valid(root.left, min, root.val)
            else:
                return False

        return valid(root, min, max)


        
        