class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not firstList or not secondList: return []
        '''
        [[2,6], [8,10], [8,15], [12,20]]
        -> [[8, 10]]
        '''
        combined_list = firstList + secondList
        combined_list.sort()
        print(combined_list)
        prev_beg, prev_end = combined_list[0]
        output = []
        for i in range(1, len(combined_list)):
            n_beg, n_end = combined_list[i]
            if n_beg <= prev_end:
                output.append([max(n_beg, prev_beg), min(n_end, prev_end)])
            prev_beg, prev_end = min(combined_list[i][0], prev_beg), max(combined_list[i][1], prev_end)
        return output

