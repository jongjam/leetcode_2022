class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Reversing it would sense but reversing it to two times seem kind of stupid
        def reverse(head) :
            prev = None
            while head is not None:
                cur = head
                head = head.next
                cur.next = prev
                prev = cur

            return prev

        copy = reverse(head)
        dummy = copy
        count = 1
        prev = None

        while dummy is not None :
            if count == n :
                print('fuck')
                if (prev is not None) :
                    prev.next = dummy.next
                    dummy = dummy.next
                else :
                    return reverse(dummy.next)
                return reverse(copy)
            count += 1
            prev = dummy
            dummy = dummy.next


        return copy
