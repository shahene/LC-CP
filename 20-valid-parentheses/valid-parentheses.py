class Solution:
    def isValid(self, s: str) -> bool:
        '''
        stack = []
        input string is valid if open brackets must match closing brackets
        [({})]
        most recent closing bracket added to stack
        pop most recent 
        '''
        bracket_map = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        stack = []
        for bracket in s:
            if bracket in bracket_map:
                stack.append(bracket)
            else:
                if stack:
                    b = stack.pop()
                    b_closing = bracket_map[b]
                    if b_closing != bracket: return False
                else:
                    return False
        return len(stack) == 0
