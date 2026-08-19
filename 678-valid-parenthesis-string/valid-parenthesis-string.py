class Solution:
    def checkValidString(self, s: str) -> bool:
        '''
        
        '''
        stack_char, stack_star = [], []

        for i, n in enumerate(s):
            if n == '(':
                stack_char.append(i)
            elif n == '*':
                stack_star.append(i)
            else:
                if stack_char: stack_char.pop()
                elif stack_star: stack_star.pop()
                else: return False

        while stack_star and stack_char:
            index_star, index_char = stack_star.pop(), stack_char.pop()
            if index_star < index_char: return False

        return len(stack_char) == 0
            