class Solution:
    def longestValidParentheses(self, s: str) -> int:
        answer = 0
        parentheses = {}   # key : 이전 단계의 미완결 '('의 갯수 , value : 시작 위치
        prevBracketNum = 0
        for i, char in enumerate(s):
            if char == "(":
                if prevBracketNum not in parentheses.keys():
                    parentheses[prevBracketNum] = i
                prevBracketNum += 1

            elif char == ")":
                if prevBracketNum == 0:
                    parentheses = {}  # key : 이전 단계의 미완결 '('의 갯수 , value : 시작 위치
                    prevBracketNum = 0
                else:
                    prevBracketNum -= 1
                    if prevBracketNum in parentheses.keys():
                        answer = max(answer, i -parentheses[prevBracketNum]+1)
        print(answer)
        return answer

sol = Solution()
# sol.longestValidParentheses(")()())")
# sol.longestValidParentheses("(()")
sol.longestValidParentheses("(())()(()((")

#  '())()(()'
# '(())()(()'