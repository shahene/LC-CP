# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        input: two non empty linked lists (heads)
        output: linked list that represents the sum

        edge case: 9, 9, 9, 9  9, 9, 9, 9

        plan
        5 + 2 => 7 
        6 + 4 => 0
        carry=

        Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
        Output: [8,9,,9,9 0,0,0,1]

        carry = 0
        while carry or l1 or l2:
            value = l1.val + l2.val
            if value > 9:
                take least significant digit
                using modulo operator 
                // 
            else:
                add to new linked list
        return new linked list
        '''
        carry = 0
        dummy = ListNode(-1)
        curr = dummy
        while carry or l1 or l2:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            current_sum = l1_val + l2_val + carry
            
            if current_sum > 9:
                lsd = current_sum % 10
                curr.next = ListNode(lsd)
                msd = current_sum // 10
                carry = msd
            else:
                curr.next = ListNode(current_sum)
                carry = 0
            curr = curr.next
            if l1:
                l1 = l1.next 
            if l2:
                l2 = l2.next

        return dummy.next