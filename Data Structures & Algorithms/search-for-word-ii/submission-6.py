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

            
            for dr, dc in directions:
                new_i = i + dr
                new_j = j + dc

                if 0 <= new_i < len(board) and 0 <= new_j < len(board[0]) and not (new_i, new_j) in visited:
                    new_c = board[new_i][new_j]
                    if new_c in temp.children:
                        visited.add((new_i, new_j))
                        dfs(new_i, new_j, temp.children[new_c], str(path + new_c))
                        visited.remove((new_i, new_j))

        for temp in root.children.keys():
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == temp:
                        visited.add((i, j))
                        dfs(i, j, root.children[temp], temp)
                        visited.remove((i, j))

        return res