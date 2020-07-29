# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        length = 1
        temp = head
        while temp.next is not None:
            temp = temp.next
            length+= 1

        temp = head
        if n == length:
            head = temp.next
        else:
            for i in range(length - n - 1):
                temp = temp.next

            if n == 1:
                temp.next = None
            else:
                temp.next = temp.next.next

        return head


val5 = ListNode(5)
val4 = ListNode(4, val5)
val3 = ListNode(3, val4)
val2 = ListNode(2, val3)
val1 = ListNode(1, val2)


sol = Solution()
sol.removeNthFromEnd(val1, 1)