# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        def bfs(root):
            if not root:
                return []
            res = []
            q.append(root)
            while q:
                li = []
                for i in range(len(q)):
                    node =  q.popleft()
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                    
                    li.append(node.val)
                res.append(li)
            return res
        return bfs(root)
        

