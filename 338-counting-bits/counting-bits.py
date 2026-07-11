class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n + 1):
            tot = 0
            bitpatt = i
            while bitpatt:
                bit = bitpatt & 1
                if bit == 1:
                    tot += 1
                bitpatt = bitpatt >> 1

            res.append(tot)
        return res