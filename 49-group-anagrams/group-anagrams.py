class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        sorted_map = collections.defaultdict(list)
        for n in strs:
            n_sorted = ''.join(sorted(n))
            sorted_map[n_sorted].append(n)
        
        for j in sorted_map:
            el = []
            for n in sorted_map[j]:
                el.append(n)
            ans.append(el)
        return ans