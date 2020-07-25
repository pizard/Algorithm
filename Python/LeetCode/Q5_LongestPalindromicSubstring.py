class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            answer = s
        elif len(s) == 0:
            answer = ""
        else:
            answer = s[0]


        for splitPos in range(1, len(s)):
            # even
            lp = splitPos-1
            rp = splitPos
            while 0 <= lp and rp < len(s) and s[lp] == s[rp]:
                # print("lp : ", lp, " rp : ", rp)
                if len(answer) < rp-lp+1:
                    answer = s[lp:rp+1]
                lp -= 1
                rp += 1


            # odd
            lp = splitPos-1
            rp = splitPos+1
            while 0 <= lp and rp < len(s) and s[lp] == s[rp]:
                # print("lp : ", lp, " rp : ", rp)
                if len(answer) < rp-lp+1:
                    answer = s[lp:rp+1]
                lp -= 1
                rp += 1

        return answer




sol = Solution()


# sol.longestPalindrome("babad") # bab
# sol.longestPalindrome("cbbd") # bb
#
# sol.longestPalindrome("abcba") # abcba
# sol.longestPalindrome("a")
# sol.longestPalindrome(" ")
# sol.longestPalindrome("  ")
sol.longestPalindrome("ccc")
# sol.longestPalindrome("ccccc")