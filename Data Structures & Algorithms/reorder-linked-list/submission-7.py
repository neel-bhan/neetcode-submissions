# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        ret = head
        first = head
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next

        cur = second
        prev = None

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        second = prev
        slow.next = None

        while second:
            nf = first.next
            ns = second.next
            first.next = second
            second.next = nf
            first = nf
            second = ns
        


