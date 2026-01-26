class Solution:
    def isValid(self, s: str) -> bool:
        '''
        stack method
        {
            '(': ')
        }
        '''
        char_map = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        stack = []
        for n in s:
            if n in char_map:
                stack.append(n)
            else:
                if not stack: return False
                closing = char_map[stack.pop()]
                if closing != n: return False
        if not stack: return True
        return False
