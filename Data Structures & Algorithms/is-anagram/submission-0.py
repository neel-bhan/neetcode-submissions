class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ret = [0] * 26
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            ret[ord(s[i]) - ord('a')] += 1
            ret[ord(t[i]) - ord('a')] -= 1
        return ret == [0] * 26