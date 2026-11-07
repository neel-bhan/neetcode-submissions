# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        res = []
        q = collections.deque()
        q.append(root)
        if not root:
            return []
        while q:
            print(q)
            level = None
            num = len(q)
            for i in range(num):
                node = q.popleft()
                if node:
                    level = node.val
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            
            res.append(level)
        return res


        
        