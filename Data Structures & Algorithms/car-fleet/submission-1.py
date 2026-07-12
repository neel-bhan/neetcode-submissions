class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ps = [(p, s) for p, s in zip(position, speed)]
        ps.sort(reverse=True)
        stack = []
        for p, s in ps:
            if stack and stack[-1] >= (target - p)/s:
                continue
            else:
                stack.append((target - p)/s)
                print(stack)
        return len(stack)