class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        c = Counter(s)
        i = 0
        res = 0
        cur = set(s[0])
        res_arr = []
        while True:
            
            if not cur:
                res_arr.append(res)
                res = 0
                if i >= len(s):
                    break
                cur.add(s[i])
            
            res += 1
            if not s[i] in cur:
                cur.add(s[i])
            c[s[i]] -= 1
            if c[s[i]] == 0:
                cur.remove(s[i])
            i+=1
        return res_arr

            
            
