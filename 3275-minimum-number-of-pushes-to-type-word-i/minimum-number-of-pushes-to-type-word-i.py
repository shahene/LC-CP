import collections
class Solution:
    def minimumPushes(self, word: str) -> int:
        '''
        understand
        input: string containing distinct english letters
        output: integer minimum number of times key will be pushed to type to the string word

        match:
        hashmap

        need to create a new mapping 
        keys numbered 2-9 to distinct collections of letters
        the keys can be remapped to any amunt of letters
        but each letter must be mapped to exactly one key

        1, *, #, and 0 do not map to any letters

        8 possible keys
        word = "abcde"
        if len(word) <= 8: return len(word)

        otherwise
        "xycdefghij"
        
        2-x,i
        3-y,j
        4-c
        5-d
        6-e
        7-f
        8-g
        9-h

        '''
        word_length, offset, count = len(word), 0, 0
        phone_mapping = collections.defaultdict(list)
        index = 0
        # build mapping
        while word_length:
            for i in range(2, 10):
                if word_length == 0: break
                phone_mapping[i].append(word[index])
                index += 1
                word_length -= 1
        # count min
        word_length = len(word)
        while word_length:
            for n in phone_mapping:
                length_phone_mapping = len(phone_mapping[n])
                offset = 0
                for i in range(length_phone_mapping):
                    count += (offset + 1)
                    offset += 1
                    word_length -= 1
                    if word_length == 0: return count
        return count

        