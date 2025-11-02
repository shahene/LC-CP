# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        num_count = collections.Counter(nums)
        dummy = ListNode(-1)
        output = []
        cur = dummy
        while head:
            if head.val not in num_count:
                output.append(head.val)
            head = head.next
        for n in output:
            cur.next = ListNode(n)
            cur = cur.next
        return dummy.next