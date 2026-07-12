class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for i in strs:
            l = len(i)
            res += str(l) + '#' + i
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        index = 0
        res = []

        while index < len(s):
            l= ""
            while self.isNum(s[index]):
                l += s[index]
                index+=1
            index += 1
            print(l)
            if index > len(s):
                break
            r = index + int(l)
            print(s[index:r])
            res.append(s[index:r])
            index = r
        return res




    def isNum(self, ch):
        return ord(ch) >= ord('0') and ord(ch) <= ord('9')

