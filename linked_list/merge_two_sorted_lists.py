# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # So a while loop to compare and sort out the two full lists
        # Another loop to take care of any remainders
        res = ListNode()
        runner = res

        # while both are not null keep comparing. this will leave a remainder
        while list1 is not None and list2 is not None :
            if list1.val < list2.val :
                runner.next = list1
                list1 = list1.next
            else :
                runner.next = list2
                list2 = list2.next
            runner = runner.next

        runner.next = list2 if list1 is None else list1

        return res.next
