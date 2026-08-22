class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        first_group, second_group, third_group = {2, 3, 4, 5}, {4, 5, 6, 7}, {6, 7, 8, 9}
        count = 0
        reserved_rows = collections.defaultdict(set)
        for res in reservedSeats:
            r, seat = res
            reserved_rows[r].add(seat)
        for row in reserved_rows:
            first_g, second_g, third_g = True, True, True
            for seat_res in reserved_rows[row]:
                if seat_res in first_group: first_g = False
                if seat_res in second_group: second_g = False
                if seat_res in third_group: third_g = False
            if (first_g and third_g):
                count += 2
            elif first_g or second_g or third_g:
                count += 1
        count += ((n - len(reserved_rows)) * 2)
        return count
