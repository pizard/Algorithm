# https://leetcode.com/problems/container-with-most-water/

### Fail


class Node:
    def __init__(self, height = -1, index = -1):
        self.height = height
        self.index = index
class Solution:
    def maxArea(self, heights) -> int:

        first = Node()
        second = Node()
        for i, height in enumerate(heights):
            node = Node(height, i)
            if node.height > second.height:
                if node.height > first.height:
                    second = first
                    first = node
                else:
                    second = node

        if first.index > second.index:
            left = second
            right = first
        else:
            left = first
            right = second

        leftIndex = left.index
        rightIndex = right.index
        result = (rightIndex-leftIndex) * second.height

        for i in range(leftIndex, -1, -1):  # enumerate + range 안되나?
            leftValue = (right.index-i) * min(heights[i], right.height)
            if leftValue > result:
                left = Node(heights[i], i)
                result = leftValue

        for i in range(rightIndex, len(heights)):
            rightValue = (i-left.index) * min(heights[i], left.height)
            if rightValue > result:
                right = Node(heights[i], i)
                result = rightValue

        return result



solution = Solution()
# print(solution.maxArea([1,8,6,2,5,4,8,3,7]))
# print(solution.maxArea([1,2]))
# print(solution.maxArea([1,2,4,3]))
# print(solution.maxArea([9,6,14,11,2,2,4,9,3,8]))
print(solution.maxArea([8,10,14,0,13,10,9,9,11,11]))

# 72 vs 80
# 32 (8 x 4) vs 30 (10 x 3)
# 72 (8 x 9) vs 80 (10 x 8)