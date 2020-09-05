# Sorted Linked List
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

class SortedLinkedList: # ascending
    def __init__(self):
        self.head = None
    def append(self,  value):
        # head가 비어있는 경우
        if self.head is None:
            self.head = Node(value)
            return

        # head가 교체되는 경우
        if value < self.head.value:
            node = Node(value)
            node.next = self.head
            self.head = node
            return

        # 일반적인 경우
        node = self.head
        while node.next is not None and value >= node.next.value:
            node = node.next

        # node.next의 위치에 새로운 node 삽입
        newNode = Node(value)
        newNode.next = node.next
        newNode.next = newNode

        return



class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def append(self, value):
        if self.head is None:
            self.head = DoubleNode(value)
            self.tail = self.head
            return

        self.tail.next = DoubleNode(value)
        self.tail.next.previous = self.tail
        self.tail = self.tail.next
        return


class SortedDoublyLinkedList: # ascending
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        if self.head is None:
            self.head = DoubleNode(value)
            self.tail = self.head
            return

        node = self.head
        while node.next is not None and value >= node.next.value:
            node = node.next


        newNode = DoubleNode(value)


        newNode.next = node.next
        if newNode.next is not None: node.next.previous = newNode

        node.next = newNode
        newNode.previous = node

        if newNode.next is None:
            self.tail = newNode

            return


        """ 아래의 코드의 경우 제대로 실행이 되지 않음 이유가 무엇일까?
        newNode.next = node.next
        node.next = newNode

        node.next.previous = newNode
        newNode.previous = node
        """


def makeBinaryTree(treeList):
    if len(treeList) == 0:
        return None
    root = TreeNode(treeList.pop(0))
    checkNodes = [root]
    while(treeList):
        checkNode = checkNodes.pop(0)
        checkNode.left = TreeNode(treeList.pop(0))
        checkNodes.append(checkNode.left)
        checkNode.right = TreeNode(treeList.pop(0))
        checkNodes.append(checkNode.right)
    return root





sdll = SortedDoublyLinkedList()
sdll.append(1)
sdll.append(4)
sdll.append(2)
sdll.append(5)
sdll.append(3)

breakpoint
