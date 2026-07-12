class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        n = len(tokens)
        stack = []
        for t in tokens:
            if t == '+':
                stack.append(stack.pop() + stack.pop())
            elif t == "-":
                b, a = stack.pop(), stack.pop()
                stack.append(a - b)
            elif t == "/":
                b, a = stack.pop(), stack.pop()
                stack.append(int(a / b))
            elif t == "*":
                stack.append(stack.pop() * stack.pop())
            else:
                stack.append(int(t))
        return stack[0]