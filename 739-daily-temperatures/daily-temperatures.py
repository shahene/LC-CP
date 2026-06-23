class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # monotonic decreasing array
        answers = [0] * len(temperatures)
        stack = [] # index, temperature
        for i, n in enumerate(temperatures):
            while stack and n > stack[-1][1]:
                indx, elem = stack.pop()
                answers[indx] = i - indx
            stack.append([i, n])
        return answers