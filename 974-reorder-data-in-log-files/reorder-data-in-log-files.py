class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs, digit_logs = [], []
        for log in logs:
            first_content = log.split()[1]
            if first_content.isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append(log)
        letter_logs.sort(key=lambda x: (x.split(' ', 1)[1], (x.split()[0])))
        return letter_logs + digit_logs
