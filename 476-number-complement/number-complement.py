class Solution:
    def findComplement(self, num: int) -> int:
        bitmask = 0
        temp = num
        while temp:
            bitmask = bitmask << 1
            bitmask = bitmask | 1
            print(bitmask)
            
            temp = temp >> 1
        return bitmask ^ num

        