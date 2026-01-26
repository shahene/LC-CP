# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        given the heads of two sorted linked lists list1 and list2
        merge the two sorted lists into one sorted list

        '''
        dummy = ListNode(-1)
        current = dummy
        while list1 and list2:
            list1_val, list2_val = list1.val, list2.val
            if list1_val < list2_val:
                current.next = ListNode(list1_val)
                list1 = list1.next
            else:
                current.next = ListNode(list2_val)
                list2 = list2.next
            current = current.next
        if list1:
            current.next = list1
        if list2:
            current.next = list2
        return dummy.next

        