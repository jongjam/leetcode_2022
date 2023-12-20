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
    
        stack = deque()
        
        while second_half is not None :
            stack.append(second_half)
            second_half = second_half.next
        
        dummy = head

        while dummy is not None and stack :
            cur = dummy.next
            dummy.next = stack.pop()
            dummy = dummy.next
            dummy.next = cur
            dummy = dummy.next


