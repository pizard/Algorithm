class Solution:
    def longestConsecutive(self, nums) -> int:
        # 소ㄹ루션
        s = set(nums)
        max_length = 0

        for n in nums:
            if n-1 not in s:
                curr_length = 1

                while n+1 in s:
                    n += 1
                    curr_length += 1

                max_length = max(max_length, curr_length)

        return max_length


sol = Solution()
sol.longestConsecutive([100, 4, 200, 1, 3, 2])