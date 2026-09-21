# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    
        def deepa(node: TreeNode) -> (int, int):
            if node.left == None and node.right == None:
                return (0, 0)
            # don't forget off by 1
            (left, lmax) = (-1, 0) if node.left == None else deepa(node.left)
            left += 1
            (right, rmax) = (-1, 0) if node.right == None else deepa(node.right)
            right += 1

            newmax = max(lmax, rmax, left + right)
            return (max(left, right), newmax)

        if root == None:
            return 0
        else:
            (_, res) = deepa(root)        
            return res
