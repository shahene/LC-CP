class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        aet: [eat, tea]
        '''
        anagram_map = collections.defaultdict(list)
        for n in strs:
            n_sorted = tuple(sorted(n))
            anagram_map[n_sorted].append(n)
        res = []
        for n in anagram_map:
            res.append(anagram_map[n])
        return res 