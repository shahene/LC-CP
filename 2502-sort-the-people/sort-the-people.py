class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        name_map = collections.defaultdict(str)
        for i, n in enumerate(heights):
            name_map[n] = names[i]
        heights.sort(reverse=True)
        output = [name_map[h] for h in heights]
        return output