# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        input: head of a linked list
        output: reversed list

        edge cases: given 1 node as linkedlist
        provided Node Class:
        class Listnode:
            def __init__(self, value, next=None):
                self.value = value
                self.next = next
        
        use a prev pointer to reasssign next pointers from the beginning of the list
        prev = None
        tmp = current_node.next
        current_node.next = prev
        prev = current_node
        current_node = tmp

        return prev at the end
        
        '''
        current = head
        prev = None
        while current:
            tmp = current.next
            current.next = prev
            prev = current
            current = tmp
        return prev