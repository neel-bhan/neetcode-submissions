# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if(self.same(root, subRoot)):
            return True
        return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)
    def same(self, l, r):
        if not l and not r:
            return True
        if l and r and l.val == r.val:
            return self.same(l.left, r.left) and self.same(l.right, r.right)
        return False