class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_len = 0 # 최대 길이
        tracker = {0: -1} # key : 이 ')'의 갯수, value : 시작 위치
        counter = 0 # 남은 ')'의 갯수
        counter_prev = 0 # 이전 counter

        for i, char in enumerate(s):
            if char == '(':
                counter += 1
            elif char == ')':
                counter -= 1
            else:
                pass

            if counter not in tracker or counter_prev < counter: # 현재 남은 ')' 갯수가 이전에 없는 경우(완전 형태가 아닌 경우) or 이번이 (인 경우
                tracker[counter] = i
            else:
                max_len = max(max_len, i - tracker[counter])

            counter_prev = counter



        print(max_len)
        return max_len


sol = Solution()

sol.longestValidParentheses("()()()())")
# sol.longestValidParentheses("(())()(()((")
# sol.longestValidParentheses(")()())")
# sol.longestValidParentheses("(()")