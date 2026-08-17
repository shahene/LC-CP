class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] < 9:
            digits[-1] += 1
            return digits


        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            tot = digits[i] + carry
            if tot > 9:
                digits[i] = 0
                carry = 1
            else:
                digits[i] = tot
                return digits

        res = [0] * (len(digits) + 1)
        print(res)
        print(digits)
        res[0] = 1
        print(res)
        for i in range(1, len(digits)):
            res[i] = digits[i - 1]
        return res