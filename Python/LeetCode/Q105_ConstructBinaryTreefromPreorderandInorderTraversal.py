# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder, inorder) -> TreeNode:
        if preorder == []:
            return None
        root = self.makeTree(preorder, inorder)
        return root
    def makeTree(self, preorder, inorder):
        if preorder == []:
            return None
        nodeVal = preorder.pop(0)
        node = TreeNode(nodeVal)
        if preorder == []:
            return node
        prevIn, nextIn = inorder[:inorder.index(nodeVal)], inorder[inorder.index(nodeVal)+1:]
        prevPre, nextPre = preorder[:len(prevIn)], preorder[len(prevIn):]

        node.left = self.makeTree(prevPre, prevIn)
        node.right = self.makeTree(nextPre, nextIn)
        return node

sol = Solution()
sol.buildTree(preorder = [3,9,20,15,7], inorder = [9,3,15,20,7])
sol.buildTree([1,2], [2,1])