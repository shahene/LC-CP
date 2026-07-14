# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        input: head of linked list
        output: new head of reversed linked list

        edge cases: given no head, 1 node in l.l.

        we can use a prev pointer to reassign
        new next pointers (imagine linked list was reversed, what would be next pointers of the nodes that we traverse through in their current order)

        1 => None
        2 => 1
        3 => 2

        use prev to keep track of prev node
        assign current node's next pointer to prev
        update prev to current node
        move current node up

        return prev at the end
        '''
        prev = None
        current = head
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        return prev