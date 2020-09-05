# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode):
        cDepthNode = [root]
        answers = []
        if root == [] or root == None:
            return []

        while cDepthNode != []:
            pDepthNode = []
            answer = []
            for i in cDepthNode:
                answer.append(i.val)
                if i.left:
                    pDepthNode.append(i.left)
                if i.right:
                    pDepthNode.append(i.right)
            answers.append(answer)
            cDepthNode = pDepthNode.copy()
        return answers