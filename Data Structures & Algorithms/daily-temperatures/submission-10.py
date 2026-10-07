class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                i1, t1 = stack.pop()
                print(i1, i)
                res[i1] = i - i1
            stack.append((i, t))
        return res