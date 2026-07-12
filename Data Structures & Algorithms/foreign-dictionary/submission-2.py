class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        d = {c: set() for word in words for c in word}
        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i+1]
            dif = False
            l = min(len(w1), len(w2))
            for j in range(l):
                c1, c2 = w1[j], w2[j]
                if c1 != c2:
                    d[c1].add(c2)
                    dif = True  
                    break
            if not dif and len(w2) < len(w1):
                return ""

        visit = {}
        res = []
        def dfs(c):
            if c in visit:
                return visit[c]
            visit[c] = True
            for nei in d[c]:
                if dfs(nei):
                    return True
            visit[c] = False
            res.append(c)
            return False

        for c in d:
            if dfs(c):
                return ""
        return "".join(res[::-1])


        