# Rule
#   전체 문자를 커버해야 함
# Input
#   s : input string
#       empty 가능, a-z
#   p : pattern
#       a-z, . or *
#       . : any single character
#       * : 0+
# Output
#

import re
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if re.compile(p+"$").match(s) is None:
            return False
        else:
            return True



sol = Solution()
# sol.isMatch("aab", "c*a*b")
print(sol.isMatch("aa", "a"))

