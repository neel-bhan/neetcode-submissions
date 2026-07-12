class Solution:
    def trap(self, height: List[int]) -> int:
        pre = []
        post = []
        for i in range(len(height)):
            if pre:
                pre.append(max(height[i], pre[-1]))
            else:
                pre.append(height[i])
            if post:
                post.insert(0, max(height[len(height)- i-1], post[0]))
            else:
                post.append(height[len(height) -1])
        res = 0
        print(pre, post)
        for index, j in enumerate(height):
            if min(pre[index], post[index]) - j > 0:
                res += min(pre[index], post[index]) - j
        return res

        