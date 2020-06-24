# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        result = ListNode()
        result_tail = result
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            carry, rest = divmod(val1 + val2 + carry, 10)
            result_tail.next = ListNode(rest)
            result_tail = result_tail.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return result.next


solution = Solution()




#
#
# result = ListNode()
# result_tail = result
# carry = 0
#
# while l1 or l2 or carry:
#     val1 = (l1.val if l1 else 0)
#     val2 = (l2.val if l2 else 0)
#     carry, out = divmod(val1 + val2 + carry, 10)
#
#     result_tail.next = ListNode(out)
#     result_tail = result_tail.next
#
#     l1 = (l1.next if l1 else None)
#     l2 = (l2.next if l2 else None)
#
# return result.next



import copy
def makeListNode(values):
    # case 1 : shallow copy (X)
    result1 = ListNode(0)
    for value in values:
        result1.next = ListNode(value)
        result1 = result1.next

    # case 2 : shallow copy (O)
    result2 = ListNode(0)
    result_tail = result2
    for value in values:
        result_tail.next = ListNode(value)
        result_tail = result_tail.next

    # case 3 : deep copy (X)
    result3 = ListNode(0)
    result_tail = copy.deepcopy(result3)
    for value in values:
        result_tail.next = ListNode(value)
        result_tail = result_tail.next

    # Q. 왜 이런 결과가 나왔을까?
    # Hint 얕은 복사(shallow copy) vs 깊은 복사(deep copy)
    return result2


print(solution.addTwoNumbers(makeListNode([2,4,3]), makeListNode([5,6,4])))
