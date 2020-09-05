# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def makeBinaryTree(treeList):
    if len(treeList) == 0:
        return None
    root = TreeNode(treeList.pop(0))
    checkNodes = [root]
    while(treeList):
        checkNode = checkNodes.pop(0)
        checkNode.left = TreeNode(treeList.pop(0))
        checkNodes.append(checkNode.left)
        if treeList != []:
            checkNode.right = TreeNode(treeList.pop(0))
            if checkNode.right:
                checkNodes.append(checkNode.right)
    return root




class Solution:
    def flatten(self, root: TreeNode) -> None:
        if root == None:
            return
        self.leftToRight(root)

    def leftToRight(self, node):
        if node.left:
            l = node.left
            r = node.right
            temp = l
            while temp.right or temp.left:
                if temp.left:
                    self.leftToRight(temp)
                temp = temp.right
            node.right = l
            temp.right = r
            if temp.right:
                self.leftToRight(temp.right)
            node.left = None
        elif node.right:
            self.leftToRight(node.right)






sol = Solution()
# sol.flatten(makeBinaryTree([1,2,5,3,4,None,6]))
# sol.flatten(makeBinaryTree([1,2,None,3]))
sol.flatten(makeBinaryTree([2,1,4,None,None,3]))


