# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        node = dummy = ListNode()
        node.next = head
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #fast.next = None
        second = slow.next
        slow.next = None
        prev = None
        cur = second

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        second = prev
        first = head

        while second:
            t1 = first.next
            t2 = second.next

            first.next = second
            second.next = t1

            first = t1
            second = t2

        

        