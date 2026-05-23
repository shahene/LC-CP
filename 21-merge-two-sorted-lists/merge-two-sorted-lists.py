# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        curr = dummy
        while list1 and list2:
            val_1, val_2 = list1.val, list2.val
            if val_1 < val_2:
                curr.next = ListNode(val_1)
                list1 = list1.next
            else:
                curr.next = ListNode(val_2)
                list2 = list2.next
            curr = curr.next
        while list1:
            val_1 = list1.val
            curr.next = ListNode(val_1)
            list1 = list1.next
            curr = curr.next
        while list2:
            val_2 = list2.val
            curr.next = ListNode(val_2)
            list2 = list2.next
            curr = curr.next
        return dummy.next


