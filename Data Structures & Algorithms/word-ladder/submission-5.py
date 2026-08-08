class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        d = defaultdict(list)
        wordList.append(beginWord)

        for w in wordList:
            for i in range(len(w)):
                d[w[:i] +"*" + w[i+1:]].append(w)
        res = 1
        seen = set()

        qu = deque()
        qu.append(beginWord)
        seen = set()
        while qu:
            
            for i in range(len(qu)):
                word = qu.popleft()
                if word == endWord:
                    return res
                
                for i in range(len(word)):
                    for nei in d[word[:i] +"*" + word[i+1:]]:
                        if nei in seen:
                            continue
                        
                        qu.append(nei)
                        seen.add(nei) 
            res += 1   
        return 0



        '''
        def dfs(word, prev):
            nonlocal res
            if word == endWord:
                return True
            if word in seen:
                return False
            seen.add(word)
            for i in range(len(word)):
                for nei in d[word[:i] +"*" + word[i+1:]]:
                    res += 1
                    if nei == prev:
                        continue
                    if dfs(nei, word):
                        print(word)
                        return True
                    res -=1
        '''
                
        






