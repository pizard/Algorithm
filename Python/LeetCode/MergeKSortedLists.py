# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



def doubleListToNode(lists):
    result = []
    for list in lists:
        resultTemp = ListNode()
        node = resultTemp
        for value in list:
            node.next = ListNode(value)
            node = node.next
        result.append(resultTemp.next)
    return result



class Solution:
    def mergeKLists(self, lists) -> ListNode:
        for i in range(len(lists)-1, -1, -1):
            if lists[i] is None:
                lists.pop(i)

        result = ListNode()
        node = result
        minValue = -1
        while len(lists) != 0:
            for i in range(0, len(lists)):
                if i == 0 or lists[i].val < minValue:
                    minValue = lists[i].val
                    minIndex = i

            node.next = ListNode(minValue)
            node = node.next

            lists[minIndex] = lists[minIndex].next
            if lists[minIndex] is None:
                lists.pop(minIndex)

        return result.next



solution = Solution()
# solution.mergeKLists(doubleListToNode([[1, 4, 5],[1, 3, 4],[2, 6]]))
solution.mergeKLists(doubleListToNode([[],[1]]))

