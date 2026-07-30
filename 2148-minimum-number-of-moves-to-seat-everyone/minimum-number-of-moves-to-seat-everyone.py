class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        min_count = 0
        for i, j in zip(seats, students):
            min_count += (abs(i - j))
        return min_count