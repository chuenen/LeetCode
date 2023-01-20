# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 and list2:
            if list1.val <= list2.val:
                next1 = list1.next
                next2 = list2.next
                if next1 and next1.val >= list2.val or not next1:
                    list1.next = ListNode(val=list2.val, next=next1)
                else:
                    next2 = list2
                self.mergeTwoLists(next1, next2)
            else:
                list1 = self.mergeTwoLists(list2, list1)
        else:
            if list2:
                return list2
        return list1
