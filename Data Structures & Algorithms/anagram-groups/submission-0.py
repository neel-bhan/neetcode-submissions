class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for i in strs:
            add = [0] * 26
            for j in i:
                add[ord(j) - ord('a')] += 1
            d[tuple(add)].append(i)
        return list(d.values())