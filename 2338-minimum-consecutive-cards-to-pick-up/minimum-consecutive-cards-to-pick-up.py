class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        '''
        given an integer array cards where cards[i] represents the value of the ith card
        pair is matching if same value

        return min number of consecutive cards you have to pick up to have a pair of matching cards among the picked cards
        if impossibe: return -1
        '''
        min_match_length = math.inf
        l = 0
        card_map = collections.defaultdict(int)
        for r in range(len(cards)):
            current_card = cards[r]
            card_map[current_card] += 1
            while card_map[current_card] > 1:
                min_match_length = min(min_match_length, r - l + 1)
                left_card = cards[l]
                card_map[left_card] -= 1
                l += 1
        return -1 if min_match_length == math.inf else min_match_length
