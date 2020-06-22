
# 전위순회
# 후위순회

class Node:
    def __init__(self, xVal, yVal, data):
        self.data = data
        self.xVal = xVal
        self.yVal = yVal
        self.left = self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.pre = []
        self.post = []

    def insert(self, node):
        if self.root is None: self.root = node
        else:
            tempNode = self.root
            while True:
                if tempNode.xVal < node.xVal:
                    if tempNode.right is None:
                        tempNode.right = node
                        return
                    else:
                        tempNode = tempNode.right
                elif tempNode.xVal > node.xVal:
                    if tempNode.left is None:
                        tempNode.left = node
                        return
                    else:
                        tempNode = tempNode.left
    def preOrder(self, node = None):
        if node is not None:
            self.pre.append(node.data)
            self.preOrder(node.left)
            self.preOrder(node.right)

    def postOrder(self, node= None):
        if node is not None:
            self.postOrder(node.left)
            self.postOrder(node.right)
            self.post.append(node.data)


def solution(nodeinfo):
    answer = [[]]

    # 1. Binary Tree 생성
    tree = BinarySearchTree()
    dictNode = {}
    # 1.1 y축 정렬 (descending)
    for i, list in enumerate(nodeinfo):
        if list[1] not in dictNode.keys():
            dictNode[list[1]] = [[list[0], i+1]]
        else:
            dictNode[list[1]].append([list[0], i+1])
    dictNode = sorted(dictNode.items(), key=(lambda f:f[0]), reverse=True)

    for dictNodeXY in dictNode:
        for dictNodeX in dictNodeXY[1]:
            tree.insert(Node(dictNodeX[0], dictNodeXY[0], dictNodeX[1])) # x, y, val
    # 1.2 x축 정렬 (ascending, tree insert)
    # for y, xi in dictNode.items():
    #     print(y, " : ", xi)


    tree.preOrder(tree.root)
    tree.postOrder(tree.root)


    answer = [tree.pre, tree.post]
    return answer


print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))
                    # [[7,4,6,9,1,8,5,2,3],[9,6,5,8,1,4,3,2,7]]
print(solution([[1,1]]))
print(solution([]))
