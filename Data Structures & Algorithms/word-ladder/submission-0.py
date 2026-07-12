class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        d = defaultdict(list)
        
        for i in wordList:
            for j in range(len(beginWord)):
                d[i[:j] + "*" + i[j+1:]].append(i)

          
        qu = deque([beginWord])
        visited = set()
        res = 1

        while qu:
            for num in range(len(qu)):
                cur = qu.popleft()
                if cur == endWord:
                    return res
                for j in range(len(beginWord)):
                    for temp in d[cur[:j] + "*" + cur[j+1:]]:
                        if temp in visited:
                            continue
                        visited.add(temp)
                        qu.append(temp)
            res += 1
        return 0




