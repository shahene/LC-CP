class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        input: temperatures
        output: answers list
        answers i the number of days you have to wait after the ith day 
        to get a warmer temperature

        [73, 74, 75, 71, 69, 72, 76, 73]
        answers = [0, 0, 0, 2, 1, 1, 0, 0]
        stack = [(76, 6)]
        stack = [(76, 6),]
        stack = [(temperatures[-1], len(temperatures) - 1)]
        for i in range(len(temperatures) - 2, -1, -1):
            while stack and stack[-1][0] <= temperatures[i]:
                stack.pop()
            if stack:
                answers[i] = stack[-1][1] - i
            stack.append((temperatures[i], i))

        '''
        stack = [(temperatures[-1], len(temperatures) - 1)]
        answers = [0] * len(temperatures)
        for i in range(len(temperatures) - 2, -1, -1):
            while stack and stack[-1][0] <= temperatures[i]:
                stack.pop()
            if stack:
                answers[i] = stack[-1][1] - i
            stack.append((temperatures[i], i))
        return answers
