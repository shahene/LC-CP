import collections
class Solution:
    def minimumPushes(self, word: str) -> int:
        letter_count = collections.Counter(word)
        sorted_arr = []
        for n in letter_count:
            sorted_arr.append(letter_count[n])
        sorted_arr.sort(reverse=True)
        count = 0
        for i, n in enumerate(sorted_arr):
            offset = (i // 8) + 1
            count += (n * offset)
        return count


