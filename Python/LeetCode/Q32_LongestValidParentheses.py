class Solution:
    def longestValidParentheses(self, s: str) -> int:
        answer = 0
        parentheses = {}   # key : 시작 위치 , value : 남은 '('의 갯수
        for i, bracket in enumerate(s):
            if bracket == "(":
                # 1. 기존의 값들 모두 1 추가
                for startIdx in parentheses.keys():
                    parentheses[startIdx] += 1
                if 0 not in parentheses.values():
                    parentheses[i] = 1
            else:
                for startIdx in parentheses.copy().keys():
                    if parentheses[startIdx] == 0:
                        parentheses.pop(startIdx)
                        continue
                    elif parentheses[startIdx] == 1:
                        if answer < i - startIdx + 1:
                            answer = i - startIdx + 1

                    parentheses[startIdx] -= 1 # 1씩 제거

        return answer




sol = Solution()
sol.longestValidParentheses("(())()(()((")