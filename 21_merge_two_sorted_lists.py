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
        """
