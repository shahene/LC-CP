class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        color_counter = collections.defaultdict(int)
        ball_color_map = {}
        output = []
        for i in range(len(queries)):
            ball, color = queries[i]
            if ball in ball_color_map:
                prev_color = ball_color_map[ball]
                color_counter[prev_color] -= 1
                if color_counter[prev_color] == 0:
                    del color_counter[prev_color]
            color_counter[color] += 1
            ball_color_map[ball] = color
            output.append(len(color_counter))
        return output
            
