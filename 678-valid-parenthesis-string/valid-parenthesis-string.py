class Solution:
    def checkValidString(self, s: str) -> bool:
        '''
        
        '''
        stack_char = []
        stack_star = []
        for i, n in enumerate(s):
            if n == '(':
                stack_char.append((')', i))
            elif n == '*':
                stack_star.append((n, i))
            else:
                if stack_char:
                    stack_char.pop()
                elif stack_star:
                    char, index = stack_star.pop()
                    if index > i:
                        return False
                else:
                    return False
        while stack_star and stack_char:
            char, index = stack_star.pop()
            char_1, index_1 = stack_char.pop()
            if index < index_1: return False
        return len(stack_char) == 0
            