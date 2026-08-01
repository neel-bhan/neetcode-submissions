# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = ""
        if not root:
            return res
        q = deque()
        q.append(root)
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node == None:
                    res += "n,"
                    continue
                res += str(node.val) + ","
                q.append(node.left)
                q.append(node.right)
        print(res)
        return res


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "":
            return None
        node = TreeNode()

        li = []
        i = 0
        while i < len(data)-1:
            start = i
            while data[i] != ',':
                i+=1
            if data[start:i] == "n":
                li.append(None)
            else:
                li.append(data[start:i])
            i+=1
        node = TreeNode(int(li[0]))
        dummy = node
        qu = deque()
        qu.append(node)
        i = 1
        while qu:
            node  = qu.popleft()
            if li[i]:
                node.left = TreeNode(int(li[i]))
                qu.append(node.left)
            i+=1
            if li[i]:
                node.right = TreeNode(int(li[i]))
                qu.append(node.right)
            i+=1
    
        return dummy
