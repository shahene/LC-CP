class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closing_bracket_map = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for bracket in s:
            if bracket in closing_bracket_map:
                if stack:
                    opening = stack.pop()
                    if opening != closing_bracket_map[bracket]:
                        return False
                else:
                    return False
            else:
                stack.append(bracket)
        return len(stack) == 0
