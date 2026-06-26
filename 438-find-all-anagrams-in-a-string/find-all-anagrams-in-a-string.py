class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        '''
        : s = "cbaebabacd", p = "abc"
        slide window unitl length k (length p)
        keep map of s up until then chek equality for p 
        if equal add l to array
        increment l 
        '''
        p_freq = collections.Counter(p)
        s_freq = collections.defaultdict(int)

        l = 0
        res_arr = []
        k = len(p)
        for r in range(len(s)):
            s_freq[s[r]] += 1
            if r - l + 1 == k:
                if s_freq == p_freq:
                    res_arr.append(l)
                s_freq[s[l]] -= 1
                if s_freq[s[l]] == 0:
                    del s_freq[s[l]]
                l += 1
        return res_arr
