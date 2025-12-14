class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sum_ascii_s = sum([ord(n) for n in s])
        sum_ascii_t = sum([ord(n) for n in t])
        remaining_ascii = sum_ascii_t - sum_ascii_s
        return chr(remaining_ascii)