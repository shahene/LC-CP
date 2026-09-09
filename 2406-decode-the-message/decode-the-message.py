class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        '''
        given strings key and message
        represent cipher key and secret message

        1. Use the first appearance of all 26 lowercase English letters in key as the order of the substitution table.
        2. Align the substitution table with the regular English alphabet.
        3. Each letter in message is then substituted using the table.
        4. Spaces ' ' are transformed to themselves.
        '''
        alphabet_shift = 0
        alphabet_sub = {}
        alphabet_sub[' '] = ' '
        for n in key:
            if n not in alphabet_sub:
                alphabet_sub[n] = chr(alphabet_shift + ord('a'))
                alphabet_shift += 1
        print(alphabet_sub)
        output_word = []
        for character in message:
            decoded_char = alphabet_sub[character]
            output_word.append(decoded_char)
        return ''.join(output_word)
