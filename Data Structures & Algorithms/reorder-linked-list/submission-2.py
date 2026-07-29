# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy, fast, slow = head, head, head
        last = slow
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        cur = slow.next
        slow.next = None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        while prev and dummy:
            p = prev.next
            d = dummy.next

            dummy.next = prev
            prev.next = d

            prev = p
            dummy = d

            

