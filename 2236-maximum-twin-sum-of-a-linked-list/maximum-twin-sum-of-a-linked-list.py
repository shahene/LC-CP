# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        max_sum = 0
        cur, arr_linked_list = head, []
        while cur:
            arr_linked_list.append(cur.val)
            cur = cur.next
        length_linked_list = len(arr_linked_list)
        for i in range(length_linked_list):
            possible_twin = length_linked_list - 1 - i
            if i >= 0 and i <= (length_linked_list / 2) - 1:
                twin_sum = arr_linked_list[i] + arr_linked_list[possible_twin]
                max_sum = max(max_sum, twin_sum)
        return max_sum