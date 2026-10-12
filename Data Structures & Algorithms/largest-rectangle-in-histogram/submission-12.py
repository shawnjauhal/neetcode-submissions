class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = []
        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                i1, h1 = stack.pop()
                area = (i - i1) * h1
                res = max(area, res)
                start = i1
            stack.append((start, h))
        while stack:
            i, h = stack.pop()
            area = (len(heights) - i) * h
            res = max(res, area)
        return res