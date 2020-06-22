# https://leetcode.com/problems/container-with-most-water/


class Solution:
    def maxArea(self, heights) -> int:
        result = 0
        height_dict = {}
        for i, height in enumerate(heights):
            if height not in height_dict.keys():
                height_dict[height] = [i]
            else:
                height_dict[height].append(i)

        leftIndex = len(heights)
        rightIndex = 0
        height_dict_sorted = sorted(height_dict.items(), reverse=True)
        for sortedHeight in height_dict_sorted:
            for index in sortedHeight[1]:
                if leftIndex > index:
                    leftIndex = index
                if rightIndex < index:
                    rightIndex = index

            tempValue = (rightIndex - leftIndex) * sortedHeight[0]
            if tempValue > result:
                result = tempValue

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