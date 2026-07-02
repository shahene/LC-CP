class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        queue = collections.deque([])
        dna_map = collections.defaultdict(int)
        for r in range(len(s)):
            nucleotide = s[r]
            queue.append(nucleotide)
            if r >= 9:
                sequence = ''.join(queue)
                dna_map[sequence] += 1
                queue.popleft()
        res = [n for n, i in dna_map.items() if i > 1]
        return res
