class node:
    def __init__(self):
        self.children = {}
        self.word = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = node()
        visited = set()
        for w in words:
            cur = root
            for c in w:
                if not c in cur.children:
                    cur.children[c] = node()
                cur = cur.children[c]
            cur.word = True
        res = []



        def dfs(i, j, temp, path):
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            if temp.word:
                res.append(path)
                temp.word = False
            for key in temp.children.keys():
                for dr, dc in directions:
                    if 0 <= i + dr < len(board) and 0 <= j + dc < len(board[0]) and not (i + dr, j + dc) in visited:
                        if board[i + dr][j+dc] == key:
                            visited.add((i + dr, j + dc))
                            dfs(i+dr, j + dc, temp.children[key], str(path + key))
                            visited.remove((i + dr, j + dc))

                

        for temp in root.children.keys():
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == temp:
                        visited.add((i,j))
                        dfs(i, j, root.children[temp], temp)
                        visited.remove((i,j))
        return res
