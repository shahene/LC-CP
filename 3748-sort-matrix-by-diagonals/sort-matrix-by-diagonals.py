import collections
class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n_matrix = [[0] * len(grid) for _ in range(len(grid))]
        # group by (r - c)
        group_dict = collections.defaultdict(list)
        for r in range(len(grid)):
            for c in range(len(grid)):
                group_dict[r - c].append(grid[r][c])
        # 2, 1, 0, -1, -2
        for i in group_dict:
            if i == 0 or i > 0:
                group_dict[i].sort(reverse=True)
            else:
                group_dict[i].sort()
        index = 0
        for r in range(len(grid)):
            for c in range(len(grid)):
                current_list = group_dict[r-c]
                n_matrix[r][c] = current_list[0]
                current_list.pop(0)

        return n_matrix