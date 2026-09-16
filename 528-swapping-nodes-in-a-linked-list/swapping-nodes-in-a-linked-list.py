# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur_index = 1
        curr = head
        length = 0
        beg_node = ListNode(-1)
        while curr:
            if cur_index == k:
                beg_node = curr
            cur_index += 1
            length += 1
            curr = curr.next
        end_node = ListNode(-1)
        target_index = length - k + 1
        cur_index = 1
        curr = head
        while curr:
            if cur_index == target_index:
                end_node = curr
            cur_index += 1
            curr = curr.next
        tmp = beg_node.val
        beg_node.val = end_node.val
        end_node.val = tmp

        return head