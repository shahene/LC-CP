class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        res = [0] * len(code)
        if k > 0:
            for i in range(len(code)):
                running_sum = 0
                j = i + 1
                length = 0
                while length < k:
                    print('fdj')
                    if j == len(code):
                        j = j % len(code)
                    new_i = j
                    running_sum += code[new_i]
                    length += 1
                    j += 1
                    if j == len(code):
                        j = j % len(code)
                res[i] = running_sum
            return res
        elif k == 0:
            for i in range(len(code)):
                code[i] = 0
            return code
        else:
            print('efj')
            for i in range(len(code)):
                running_sum = 0
                j = (i - 1) % len(code)
                length = 0
                while length > k:
                    new_i = j % len(code)
                    print(new_i)
                    length -= 1
                    running_sum += code[new_i]
                    j = (j - 1) % len(code)
                res[i] = running_sum
            return res
            
            