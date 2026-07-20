class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        word = s
        regex = p
        memo = {}
        def dfs(l, r):
            if l == len(regex):
                return r == len(word)

            if (l, r) in memo:
                return memo[(l,r)]
            if l + 1 < len(regex):
                if regex[l+1] == "*":
                    if r < len(word):
                        if word[r] == regex[l] or regex[l] ==".":
                            if dfs(l, r+1):
                                memo[(l,r )] = True
                                return True
                    if dfs(l+2, r):
                        memo[(l,r )] = True
                        return True
                    memo[(l,r )] = False
                    return False
            if regex[l] == ".":
                memo[(l,r)] = dfs(l + 1, r + 1)
                return memo[(l,r)]
            if r < len(word) and regex[l] == word[r]:
                memo[(l,r)] = dfs(l + 1, r + 1)
                return memo[(l, r)]
            else:
                memo[(l,r)] = False
                return memo[(l,r)]

        return dfs(0, 0)