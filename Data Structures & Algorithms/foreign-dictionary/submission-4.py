class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = defaultdict(set)
        n = len(words)
        if n == 1:
            return words[0]

        seen = set()
        chars = set()
        for word in words:
            chars.update(word)


        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            le = min(len(w1), len(w2))
            c = False
            for j in range(le):
                if w1[j] != w2[j]:
                    adj[w2[j]].add(w1[j])
                    c = True
                    break
            if not c:
                if len(w2) < len(w1):
                    return ""
        res = ""
        visit = {}
        def dfs(l):
            if l in visit:
                return visit[l]
            nonlocal res
            visit[l] = True
            for nei in adj[l]:
                if dfs(nei):
                    return True
            visit[l] = False
            res += l
            return False
        for w in chars:
            if dfs(w):
                return ""
        return res

            
            
            
