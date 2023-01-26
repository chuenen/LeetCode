# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 and list2 and list1.val > list2.val:
            list1, list2 = list2, list1
        result = list1
        
        while list2:
            if not list1:
                break
            next_ = list1.next
            if list1.val <= list2.val and (not next_ or next_ and next_.val > list2.val):         
                temp = list2.next
                list2.next = next_
                list1.next = list2
                list2 = temp
           
            else:
                list1 = list1.next

        if not list1:
            return list2
        return result
        
        """
        # Recursive
        if not (list1 and list2):
            return list1 or list2
        
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
        else:
            list1 = self.mergeTwoLists(ListNode(list2.val, list1), list2.next)
        return list1
        """
