# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #check if enough nodes avaiable
        def check(node, k):
            for i in range(k):
                if node:
                    node = node.next
                else:
                    return False
            return True

        #save first pointer and next pointer
        #make first pointer point to next pointer
        dummy = cur = ListNode(0, head)
        cur = cur.next
        prevTail = None
        first = True
        res = None
        i = 1
        while check(cur, k):
            
            old = cur
            prev = None
            for i in range(k):
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            if first:
                res = prev
                first = False
            if prevTail:
                prevTail.next = prev
            old.next = cur
            prevTail = old
     

            
        return res if res else head