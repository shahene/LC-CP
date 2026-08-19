class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        '''
        each row has 10 seats
        reservedSeats[i] = [row_i, seat_i] 
        4 person group must be assigned to four seats in the same rows
        only these seat blocks:
        seats 2, 3, 4, 5
        seats 4, 5, 6, 7
        seats 6, 7, 8, 9
        a block can be used only if none of its seats are reserved
        each seat can be assigned to at most one group
        max number of 4 seat groups

        maximum of 2 groups can sit in one given row (if no reserved seats)
        if 2 or 3 is reserved (can't sit at 2,3,4,5) so max is now one in given row
        if 4 or 5 is reserved (can't sit at 4,5,6,7) 
        if 6 or 7 is reserved (can't sit at 6,7,8,9)
        '''
        total_max = 0
        row_reserved = collections.defaultdict(set)
        for row, seat in reservedSeats:
            row_reserved[row].add(seat)
        for r in row_reserved:
            left_free, middle_free, right_free = True, True, True
            if 2 in row_reserved[r] or 3 in row_reserved[r] or 4 in row_reserved[r] or 5 in row_reserved[r]:
                left_free = False
            if 4 in row_reserved[r] or 5 in row_reserved[r] or 6 in row_reserved[r] or 7 in row_reserved[r]:
                middle_free = False
            if 6 in row_reserved[r] or 7 in row_reserved[r] or 8 in row_reserved[r] or 9 in row_reserved[r]:
                right_free = False
            if left_free and right_free:
                total_max += 2
            elif left_free or right_free or middle_free:
                total_max += 1
            else:
                continue
        total_max += ((n - len(row_reserved)) * 2)
        return total_max