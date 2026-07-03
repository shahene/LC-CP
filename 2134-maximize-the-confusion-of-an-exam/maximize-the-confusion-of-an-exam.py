class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        max_grade = 0
        # window_length - max_recurring_grade <= k:
        # while window_length - max_recurring_grade > k:
        #   increment window_length
        l = 0
        consecutive_grades = 0
        grade_map = collections.defaultdict(int)
        for r in range(len(answerKey)):
            grade = answerKey[r]
            grade_map[grade] += 1
            max_grade = max(max_grade, grade_map[grade])

            while (r - l + 1) - max_grade > k:
                left_grade = answerKey[l]
                grade_map[left_grade] -= 1
                l += 1
            consecutive_grades = max(consecutive_grades, r - l + 1)
        return consecutive_grades