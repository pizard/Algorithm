# https://leetcode.com/problems/container-with-most-water/


class Solution:
    def maxArea(self, height) -> int:
        water = 0
        head = 0
        tail = len(height) - 1

        for cnt in range(len(height)):

            width = abs(head - tail)

            if height[head] < height[tail]:
                res = width * height[head]
                head += 1
            else:
                res = width * height[tail]
                tail -= 1

            if res > water:
                water = res

        return water

solution = Solution()
# print(solution.maxArea([1,8,6,2,5,4,8,3,7]))
# print(solution.maxArea([1,2]))
# print(solution.maxArea([1,2,4,3]))
# print(solution.maxArea([9,6,14,11,2,2,4,9,3,8]))
print(solution.maxArea([8,10,14,0,13,10,9,9,11,11]))

# 72 vs 80
# 32 (8 x 4) vs 30 (10 x 3)
# 72 (8 x 9) vs 80 (10 x 8)