# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        critical_indices_array = []
        index = 0
        curr = head
        prev = None
        while curr and curr.next:
            if prev:
                current_val = curr.val
                if (current_val < prev and current_val < curr.next.val) or (current_val > prev and current_val > curr.next.val):
                    critical_indices_array.append(index)
            prev = curr.val
            curr = curr.next
            index += 1
        if len(critical_indices_array) < 2: return [-1, -1]
        minDist, maxDist = math.inf, -math.inf
        critical_indices_array.sort()
        maxDist = critical_indices_array[-1] - critical_indices_array[0]
        for i in range(1, len(critical_indices_array)):
            if critical_indices_array[i] - critical_indices_array[i-1] < minDist:
                minDist = critical_indices_array[i] - critical_indices_array[i-1]
        return [minDist, maxDist]

