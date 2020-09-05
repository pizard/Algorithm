
class Solution:
    def firstMissingPositive(self, nums) -> int:
        nums = set(nums)

        if len(nums) == 0:
            return 1

        candidates = [i for i in range(1, len(nums)+2)]
        for num in nums:
            if num > 0 and num < len(nums)+2:
                candidates.remove(num)


        return min(candidates)

sol = Solution()
print(sol.firstMissingPositive([7,8,9,11,12]))
print(sol.firstMissingPositive([7]))
print(sol.firstMissingPositive([1,2,0]))
print(sol.firstMissingPositive([1,1]))




