# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        second_half = head
        dummy = head

        while dummy is not None and dummy.next is not None:
            second_half = second_half.next
            dummy = dummy.next.next
        
        dummy = second_half
        second_half = second_half.next #now starts at the next half
        dummy.next = None
    
        # Reversing the second half for merging

        prev = None
        while second_half is not None:
            cur = second_half
            second_half = second_half.next
            cur.next = prev
            prev = cur
        #Second half now reversed
        second_half = prev
         
        dummy = head
        while dummy is not None and second_half is not None :
            cur = dummy.next
            dummy.next = second_half
            second_half = second_half.next
            dummy = dummy.next
            dummy.next = cur
            dummy = dummy.next
