import collections
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_length, number_words, res = len(words[0]), len(words), [] 
        if not words or not s or len(s) < len(words[0]): return res

        word_counter = collections.Counter(words)

        for offset in range(word_length):
            l, r = offset, offset + word_length
            valid_window_size = word_length * number_words
            running_word_map = collections.defaultdict(int)
            starting_index = offset
            while r <= len(s):

                word = s[l:r]
                running_word_map[word] += 1

                if r >= valid_window_size:
                    if running_word_map == word_counter:
                        res.append(starting_index)
                    left_word = s[starting_index: starting_index + word_length]
                    running_word_map[left_word] -= 1
                    if running_word_map[left_word] == 0:
                        del running_word_map[left_word]
                    starting_index += word_length

                l = r
                r += (word_length)
        return res
            

            
            
