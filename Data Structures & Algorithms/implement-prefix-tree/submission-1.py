class Node:
    def __init__(self):
        self.children = [None] * 26
        self.end = False


class PrefixTree:

    def __init__(self):
        self.root = Node()
        

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if cur.children[ord(c) - ord('a')]:
                cur = cur.children[ord(c) - ord('a')]
            else:
                cur.children[ord(c) - ord('a')] = Node()
                cur = cur.children[ord(c) - ord('a')]
        cur.end = True


    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if cur.children[ord(c) - ord('a')]:
                cur = cur.children[ord(c) - ord('a')]
            else:
                return False

        return cur.end
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if cur.children[ord(c) - ord('a')]:
                cur = cur.children[ord(c) - ord('a')]
            else:
                return False
        return True

        
        