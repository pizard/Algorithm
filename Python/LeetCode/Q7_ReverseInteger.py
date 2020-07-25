class Solution:
    def reverse(self, x: int) -> int:

        val = int("".join(reversed(list(str(abs(x))))))
        if x < 0:
            if -val < -2**31:
                return 0
            else:
                return -val
        else:
            if val > 2 ** 31 - 1:
                return 0
            else:
                return val
sol = Solution()
sol.reverse(-2147483648)
