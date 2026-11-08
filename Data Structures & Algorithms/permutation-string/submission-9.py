class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        ds = defaultdict(int)
        num = 0
        for c in s1:
            if c not in ds:
                num += 1
            ds[c] += 1
        
        dc = defaultdict(int)
        matched = 0
        
        for c in s2[:len(s1)]:
            if c in ds:
                dc[c] += 1
                if dc[c] == ds[c]:
                    matched += 1

        if matched == num:
            return True

        r = len(s1)
        l = 0

        while r < len(s2):
            c = s2[r]
            if c in ds:
                dc[c] += 1
                if dc[c] == ds[c]:
                    matched += 1

            remove = s2[l]

            if remove in ds:
                dc[remove] -= 1
                if dc[remove] == ds[remove] -1 :
                    matched -= 1

            if matched == num:
                return True
            
            r += 1
            l += 1
        return False



        