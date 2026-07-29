# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head_arr = []
        curr = head
        while curr:
            head_arr.append(curr.val)
            curr = curr.next
        head_arr.sort()
        dummy = ListNode(-1)
        curr = dummy
        for n in head_arr:
            n_node = ListNode(n)
            curr.next = n_node
            curr = curr.next
        return dummy.next