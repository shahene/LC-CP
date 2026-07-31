class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        '''
        input: array of strings tokens that represent an arithmetic expression in Reverse Polish Notation
        output: integer that represents the value of the expression

        valid operators => +, -, *, /
        each operand may be an integer or another expression
        division between two integers is floor division
        no division by 0
        input represents valid arithmetic expression
        answer can be represented in a 32-bit integer

        ex.
        ["2", "1", "+", "3", "*"]
        [2, 1] then operator
        2 operator 1, append result to stack
        [3, 3] 
        3 * 3 = 9

        ex2. 
        ["4", "13", "5", "/". "+"]
        [4, 13, 5]
        13 operator 5 => 2
        [4, 2]
        4 operator 2

        O(n) space + O(n) time

        pseudocode:
        stack = []
        res = 0
        iterate through tokens
            each tokens[i] if not an operator:
                append int(tokens[i]) to stack
            otherwise:
                pop twice from stack
                append the result of the operation on the two operands
                res += result
        '''
        if len(tokens) == 1: return int(tokens[0])
        stack = []
        operator_set = {'*', '+', '-', '/'}
        res = 0
        for n in tokens:
            if n not in operator_set:
                stack.append(int(n))
            else:
                operation_result = 0
                operand_one, operand_two = stack.pop(), stack.pop()
                print(operand_one, operand_two)
                if n == '*': operation_result = (operand_two * operand_one)
                if n == '-': operation_result = (operand_two - operand_one)
                if n == '/': operation_result = (int(operand_two / operand_one))
                if n == '+': operation_result = (operand_two + operand_one)
                stack.append(operation_result)
                res = operation_result
        return res
    
