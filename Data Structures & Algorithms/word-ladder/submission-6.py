class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        d = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                d[pattern].append(word)

        q = deque([(beginWord, 1)])
        seen = {beginWord}

        while q:
            word, steps = q.popleft()

            if word == endWord:
                return steps

            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]

                for nei in d[pattern]:
                    if nei not in seen:
                        seen.add(nei)
                        q.append((nei, steps + 1))

                d[pattern] = []

        return 0