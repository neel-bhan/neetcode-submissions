class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if not c in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True

    def search(self, word: str) -> bool:
        def dfs(word, cur):
            if word == "":
                return cur.word

            print(word)
            c = word[0]
            if c == ".":
                res = False
                for i in cur.children.values():
                    if dfs(word[1:], i):
                        res = True
                return res
            else:
                if not c in cur.children:
                    return False
                return dfs(word[1:], cur.children[c])
        return dfs(word, self.root)
            
        
