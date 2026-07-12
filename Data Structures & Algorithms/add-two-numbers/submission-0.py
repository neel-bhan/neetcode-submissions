# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        cur = dummy = ListNode()
        carry = False
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

            ans = v1 + v2
            if carry:
                ans +=1 
            carry = False
            if ans >= 10:
                ans -= 10
                carry = True
            
            add = ListNode(ans, None)
            cur.next = add
            cur = cur.next

        return dummy.next








            

