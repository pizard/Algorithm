# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1, l2) -> ListNode:
        result = ListNode()
        node = result
        while l1 or l2:
            if l1 is None:
                node.next = l2
                break;
            if l2 is None:
                node.next = l1
                break

            if l1.val > l2.val:
                node.next = ListNode(l2.val)
                l2 = l2.next
            else:
                node.next = ListNode(l1.val)
                l1 = l1.next

            node = node.next

        return result.next



solution = Solution()


def listToNode(list):
    result = ListNode()
    node = result
    for value in list:
        node.next = ListNode(value)
        node = node.next
    return result.next



solution.mergeTwoLists(listToNode([1,2,4]), listToNode([1,3,4]))
# solution.mergeTwoLists(listToNode([]), listToNode([0]))

