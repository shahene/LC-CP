class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        '''
        number of distinct substrings should be 2**k
        create set
        check if length of set == 2^k
        '''
        distinct_code_set = set()
        l = 0
        for r in range(len(s)):
            if r >= k - 1:
                distinct_code_set.add(s[l: r + 1])
                l += 1
        return len(distinct_code_set) == 2**k