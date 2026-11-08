class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = zip(position, speed)
        n = list(n)
        n.sort(reverse=True)

        stack = []
        for a, c, in n:
            print(a,c )


        for p, s in n:

            time = (target - p) / s
            if not stack:
                stack.append(time)

            if stack and stack[-1] < time:
                stack.append(time)
        return len(stack)
