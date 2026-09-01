# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        '''
        important point:
        min-> most adjaccent indices
        -> can have prev index variable: cur_index
        max -> first and last
        '''
        cur_index = 0
        curr = head
        prev, prev_index, last_index, first_index = None, None, None, None
        minDist, maxDist = math.inf, -math.inf
        length = 0
        while curr and curr.next:
            if prev:
                current_val = curr.val
                if (current_val < prev and current_val < curr.next.val) or (current_val > prev and current_val > curr.next.val):
                    if prev_index: minDist = min(minDist, cur_index - prev_index)
                    if not first_index: first_index = cur_index
                    prev_index = cur_index
                    last_index = cur_index
                    length += 1
            prev = curr.val
            curr = curr.next
            cur_index += 1
        if length < 2: return [-1, -1]
        maxDist = last_index - first_index
        return [minDist, maxDist]

