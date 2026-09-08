class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        '''
        items[i] = [id_i, score_i]
        represents one score from a student with ID_i
        calculate each student's top five average

        returns array of pairs result, where result[j] = [Id_j, topFiveAverage], sort result by IDj in increasing order
        '''
        item_score_map = collections.defaultdict(list)
        for i in range(len(items)):
            item_score_map[items[i][0]].append(items[i][1])
        for n in item_score_map:
            item_score_map[n] = sorted(item_score_map[n])
        output = []
        for n in item_score_map:
            index = 0
            top_five = 0
            while index < 5:
                score = item_score_map[n].pop()
                top_five += score
                index += 1
            output.append([n, top_five // 5])
        output.sort(key=lambda x: x[0])
        return output
