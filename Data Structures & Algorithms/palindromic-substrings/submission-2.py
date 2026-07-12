class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        for index in range(n):
            i = index
            j = index 
            while i >= 0 and j < n:
                if s[i] == s[j]:

                    i-=1
                    j+=1
                    count += 1
                else:
                    break
            i = index
            j = index +1

            while i >= 0 and j < n:
                if s[i] == s[j]:
                    i-=1
                    j+=1
                    count +=1
                else:
                    break   

        return count
