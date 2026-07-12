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

        while len(lists) > 1:
            new = merge(lists[0], lists[1])
            print(len(lists))
            lists.pop(0)
            lists.pop(0)
            lists.append(new)
        return lists[0] if lists else None
        
        