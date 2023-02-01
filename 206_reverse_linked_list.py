# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = ListNode()
        while head:
            tmp = head.next
            head.next = curr.next
            curr.next = head
            head = tmp     
        return curr.next

        """The second solution.
        pre = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = pre
            pre = curr
            curr = nxt
        return pre
        """
