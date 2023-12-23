# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry_out = 0
        sum = l1.val + l2.val 
        l1 = l1.next
        l2 = l2.next

        if sum >= 10 :
            sum %= 10
            carry_out = 1

        res = ListNode(sum)
        dummy = res

        while l1 and l2 :
            sum = l1.val + l2.val + carry_out
            if sum >= 10 :
                sum %= 10
                carry_out = 1
            else :
                carry_out = 0

            res.next = ListNode(sum)
            res = res.next
            l1 = l1.next
            l2 = l2.next
        
        if l1 or l2 :
            remainder = l1 if l1 else l2
            while remainder:
                sum = remainder.val + carry_out
                if sum >= 10 :
                    sum %= 10
                    carry_out = 1
                else :
                    carry_out = 0

                res.next = ListNode(sum)
                res = res.next
                remainder = remainder.next
                
        if carry_out :
            res.next = ListNode(carry_out)
            res = res.next

        return dummy
