class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        

        d = defaultdict(list)
        n = len(words)
        li = set("".join(words))
        for i in range(n):
            for j in range(i):
                w1, w2 = words[i], words[j]
                diff = False
                for c in range(min(len(w1), len(w2))):
                    if w1[c] != w2[c]:
                        d[w2[c]].append(w1[c])
                        diff= True
                        break
                if not diff and len(w2)> len(w1):
                    return ""
        res = ""
        path = set()
        seen = set()

        def dfs(c):
            print(c)
            nonlocal res
            if c in path:
                return False
            if c in seen:
                return True

            seen.add(c)
            path.add(c)
            for nei in d[c]:
                if not dfs(nei):
                    return False
            res += c
            path.remove(c)

            return True
        for c in li:
            if not dfs(c):
                return ""

        return res[::-1]


