# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        glo = 0
        d= {}
        for index, i in enumerate(inorder):
            d[i] = index
        root = TreeNode(preorder[0])
        def dfs(l, r, node):
            nonlocal glo
            if not node:
                return None
            if glo >= len(preorder):
                return None
            if l >= r:
                return None
            value = preorder[glo]
            glo += 1
            idx = d[value]
            node.val = value
            node.left = dfs(l, idx, TreeNode())
            node.right = dfs(idx + 1, r, TreeNode())
            return node

        dummy = TreeNode()
        dfs(0, len(inorder), dummy)
        return dummy

            


         
            