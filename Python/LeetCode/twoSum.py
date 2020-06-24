# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


class Solution:
    def twoSum(self, nums, target):
        checkValue = {} # key : value , value : index
        for i, num in enumerate(nums):
            n = target - num
            if n not in checkValue:
                checkValue[num] = i
            else:
                return [checkValue[n], i]


solution = Solution()
print(solution.twoSum([1,8,4,3,6,9,7], 10))
