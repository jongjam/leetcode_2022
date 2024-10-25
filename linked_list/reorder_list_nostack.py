# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head

        while fast and fast.next :
            slow = slow.next
            fast = fast.next.next
        
        dummy = slow.next
        slow.next = None
        prev = None

        while dummy :
            temp = dummy.next # save the rest of the list after reversing
            dummy.next = prev
            prev = dummy
            dummy = temp
        
        # Ok now must merge the lists
        list1 = head
        list2 = prev

        while list1 and list2:
            temp = list1.next
            list1.next = list2
            list2 = list2.next
            list1 = list1.next
            list1.next = temp
            list1 = list1.next

