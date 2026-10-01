class Solution:
    def isValid(self, s: str) -> bool:
        '''
        stack = []
        input string is valid if open brackets must match closing brackets
        [({})]
        most recent closing bracket added to stack
        pop most recent 
        '''
        stack = []
        mapp = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for char in s:
            if char not in mapp:
                stack.append(char)
            else:
                if not stack: return False
                popped_char = stack.pop()
                if mapp[char] != popped_char: return False
        return True if not stack else False


