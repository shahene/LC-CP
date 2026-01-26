class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        given an array of strings strs, group the anagrams together
        {
            aet: ['eat', 'tea']
            etc

        }
        keep dictionary where key is sorted strs[i] and value is array of all anagrams
        (including current anagram)
        return extended output list
        O(N) time, O(N) space
        '''
        anagram_map = collections.defaultdict(list)
        for n in strs:
            anagram_map[tuple(sorted(n))].append(n)
        return [n for n in anagram_map.values()]