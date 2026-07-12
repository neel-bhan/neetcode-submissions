class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, r = 0, len(s1) - 1
        a1 = [0] * 26
        a2 = [0] * 26
        
        for s in s1:
            a1[ord(s) - ord('a')] +=1
        for s in s2[0:len(s1)]:
            a2[ord(s) - ord('a')] +=1
        while r < len(s2):
            if a1 == a2:
                return True
            a2[ord(s2[l]) - ord('a')] -= 1
            l+=1
            r+=1
            if(r >= len(s2)):
                break
            a2[ord(s2[r]) - ord('a')] += 1


        return False    


        