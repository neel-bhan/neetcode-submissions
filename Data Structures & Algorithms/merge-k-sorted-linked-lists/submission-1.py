# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(l1, l2):
            dummy = cur = ListNode()

            while l1 and l2:
                v1 = l1.val if l1 else float("inf")
                v2 = l2.val if l2 else float("inf")

                if v1 >= v2:
                    cur.next = l2
                    l2 = l2.next
                else:
                    cur.next = l1
                    l1 = l1.next
                cur = cur.next
            cur.next = l1 or l2

            return dummy.next

        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedlists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i + 1 < len(lists) else None
                new = merge(l1, l2)
                mergedlists.append(new)
            lists = mergedlists
            
        return lists[0] if lists else None
        
        