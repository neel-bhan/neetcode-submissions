class Solution:
    def isValid(self, s: str) -> bool:
        o = {
            "}" : "{",
            ")" : "(",
            "]" : "["
        }
        stack = []
        for c in s:
            if stack and c in o:
                if stack.pop() != o[c]:
                    return False
            else:
                stack.append(c)
        if stack:
            return False
        return True