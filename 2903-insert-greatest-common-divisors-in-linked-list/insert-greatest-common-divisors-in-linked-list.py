# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def gcd(self, num1, num2):
        j = min(num1, num2)
        while j:
            if num1 % j == 0 and num2 % j == 0:
                return j
            j -= 1
        return head
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        if not curr.next: 
            print('j')
            return head
        prev = None
        curr = head
        while curr:
            if prev:
                gc = gcd(prev.val, curr.val)
                print(gc)
                tmp = prev.next
                node = ListNode(gc)
                prev.next = node
                node.next = curr
            prev = curr
            curr = curr.next
        return head

