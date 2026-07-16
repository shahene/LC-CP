class Solution:
    def hIndex(self, citations: List[int]) -> int:
        '''
        sort citations
        iterate until len(subarray from that index to end) is < element at that index
        '''
        if len(citations) == 1 and citations[0] >= 1: return 1
        citations.sort()
        
        n = len(citations)
        for i in range(len(citations)):
            ceiling_len = citations[i]
            if n - i <= ceiling_len:
                return n - i
        return 0
        