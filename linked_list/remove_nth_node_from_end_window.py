# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Reversing it would sense but reversing it to two times seem kind of stupid
        dummy = ListNode(99, head)
        l = dummy
        r = head
        for i in range(n) :
            r = r.next
        print(r)

        while r:
            l = l.next
            r = r.next

        l.next = l.next.next
        return dummy.next

