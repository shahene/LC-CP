# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        use fast and slow pointers
        since fast pointer is 2x the speed of slow pointer
        once fast pointer reaches end of linked list, slow pointer
        will be at the middle of the linked list.
        so, just return slow
        '''
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow