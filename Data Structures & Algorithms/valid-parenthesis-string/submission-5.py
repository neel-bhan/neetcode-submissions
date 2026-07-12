class Solution:
    def checkValidString(self, s: str) -> bool:

        left = []
        star = []
        for index, st in enumerate(s):
            if st  == "(":
                left.append(index)
            if st == "*":
                star.append(index)
            if st == ")":
                if not left and not star:
                    return False
                if left:
                    left.pop()
                else:
                    star.pop()

        while left and star:
            if left.pop() > star.pop():
                return False
            
        return not left
                

        