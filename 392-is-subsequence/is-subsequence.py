class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        curr = 0
        n = len(s)
        j = 0
        for i in range(len(t)):
            if j < n and t[i] == s[j]:
                curr += 1
                j += 1
        return curr == n
