# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 5 - 2 = 3 - 1 => index of node to remove (if we were to think of LL as an array)
        # remove by reassinging pointers of prev
        # 1, 1, 1, 1, 1, 1, 1, 1
        # len(ll) - (n - 1)
        # reassign pointers at that index
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        index = 0
        curr = head
        if length == 1 and n == 1: return None

        while index != length - (n + 1) and curr:
            index += 1
            curr = curr.next
        if curr and curr.next:
            curr.next = curr.next.next
        else:
            index = length - (n+1)
            curr = head
            while index != 0:
                curr = curr.next

                index += 1
            return curr
        return head