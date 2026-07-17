# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        input: 2 heads of two sorted lists
        output: merged linked list
        '''
    
        dummy = ListNode(0, None)
        current = dummy
        while list1 and list2:
            smaller = ListNode(0)
            if list1.val < list2.val:
                smaller.val = list1.val
                list1 = list1.next
            else:
                smaller.val = list2.val
                list2 = list2.next
            current.next = smaller
            current = current.next
            
        
        if list1:
            current.next = list1
        if list2:
            current.next = list2
        
        return dummy.next