class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        temperatures represents the daily temperatures
        return new array where answers[i] is the number of "days" you have to wait after the ith day to get a warmer temperature
        if not possible, answers[i] = 0

        input: temperatures array representing daily temperatures
        output: answers array representing the number of elements where you get a higher temperature

        edge cases: 1 temperature value => 0
                    negative temperatures ? => not possible
        
        Input: temperatures = [73,74,75,71,69,72,76,73]
        Output: [1,1,4,2,1,1,0,0]
        
        use a monotonically increasing stack

        pseudocode:
        start from the end of temperatures array
        if not stack: append temperature to stack, 0 to that element

        stack = [73]
        temperature = 76, nothing > 76, add 0 to res
                        pop 73 from stack
                        append 76 stack
        temperature = 72, stack[-1] > 72, add 1 to res
                      72 <= 76 append 72 to stack
        temperature = 69, stack[-1] (72) > 69, add 1 to res
                        69 <= stack[-1], append 69 to stack
        temperature = 71, while stack: pop from stack unitl we reach 72, keep count
                            add 2 to res
                        71 <= 72: append 71 to stack
        temperature = 75, while stack: pop from stack until we reach 76, add 4 to res
                            75 <= 76, append 75 to stack
        temperature = 74, 74 < 75, (stack[-1]) add 1 to res
                        append 74 to stack
        same w temperature = 73
        
        O(N) time + O(N) space

        rInput: temperatures = [30,60,90]
        Expected Output: [1,1,0]

        res = [0, 0, 0], stack = [90]
        temp = 60

        actual output: [1,1,4,1,1,1,0,0]

        [(73, 7)]'
        temp = 76

        stack = [(76, 6)]
        temp = 72
        [(76, 6), (72, 5)]
        temp = 69
        [(76, 6), (72, 5), (69, 4)]
        temp = 71, i = 3
        count = 1, 

        '''
        n = len(temperatures)
        res, stack = [0] * len(temperatures), [n - 1]
        print(stack)
        for i in range(n- 2, -1, -1):
            temp = temperatures[i]
            
            if temperatures[stack[-1]] > temp: 
                res[i] = 1
            else:
                count = 0
                while stack and temperatures[stack[-1]] <= temp:
                    stack.pop()
                if stack: 
                    res[i] = stack[-1] - i

            stack.append(i)
        return res