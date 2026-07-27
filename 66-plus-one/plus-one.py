class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        '''
        input: array of digits (ordered from MSB to LSB (in left to right order))
        output: array of digits after adding one arithmetically to the original input
        
        Input: digits = [19]
        Output: [2, 0]

        better to reverse array and do arithmetic with carry

        code:
        digits.reverse()
        i, carry = 0, 0
        while carry or i < len(nums):
            res = (digits[i] + 1 + carry) % 10
            carry = (res // 10)
            result_arr.append(res)
        result_arr.reverse()
        return result_arr

        input: digits = [1, 9]
        digits = [9, 1]

        result_arr = [0, 2]
        carry = 0
        result_arr = [2, 0]


        '''
        result = []
        carry = 0
        i = len(digits) - 1
        while carry or i >= 0:
            if i == len(digits) - 1:
                total = digits[i] + 1 + carry
                res = total % 10
                result.append(res)
                carry = total // 10
            elif i != len(digits) - 1 and carry:
                if i in range(len(digits)):
                    total = digits[i] + carry
                else:
                    total = carry
                res = total % 10
                result.append(res)
                carry = total // 10
            else:
                result.append(digits[i])
            i -= 1
        result.reverse()
        return result
        