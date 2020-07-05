# Rule
#   균형잡힌 문자열 : '(', ')'의 갯수가 같음
#   올바른 괄호 문자열 : '(', ')'의 짝도 모두 맞음
#   변환 과정
#       1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
#       2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다.
#       3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다.
#           3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.
#       4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다.
#           4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다.
#           4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
#           4-3. ')'를 다시 붙입니다.
#           4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
#           4-5. 생성된 문자열을 반환합니다.
# Input
#   p : 균형잡힌 괄호 문자열 ( 2 ~ 1000, 짝수 )
#       '(', ')'로 구성
# Output
#   올바른 괄호 문자열

import queue
def makeCorrectBrackets(p, ans):
    # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
    if p == "":
        ans.append("")
        return;
    bracketQueue = queue.Queue()
    bracketQueueOpposit = ""
    # 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다.
    u, v = "", ""

    _put, _get = ['(', ')'] if p[0] == '(' else [')', '(']
    for i, bracket in enumerate(p):
        if bracket == _put:
            bracketQueue.put(bracket)
            bracketQueueOpposit += _get
        elif bracket == _get:
            bracketQueue.get()
            bracketQueueOpposit += _put
        else:
            print("Error Occur")

        if bracketQueue.qsize() == 0:
            u, v = p[:i + 1], p[i + 1:]
            break;
    # print("u: ", u, " v: ", v)

    # 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다.
    if _put == '(':
        # 3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.
        ans.append(u)
        makeCorrectBrackets(v, ans)
    # 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다.
    else:
        # 4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다.
        emptyString = "("
        # 4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
        ans2 = []
        makeCorrectBrackets(v, ans2)
        emptyString += ''.join(ans2)
        # 4-3. ')'를 다시 붙입니다.
        emptyString += ")"
        # 4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
        emptyString += bracketQueueOpposit[1:len(bracketQueueOpposit)-1]
        # 4-5. 생성된 문자열을 반환합니다.
        ans.append(emptyString)
def solution(p):
    ans = []
    makeCorrectBrackets(p, ans)

    return ''.join(ans)

inputs = ["(()())()"	    # "(()())()"
    , ")("	        # "()"
    , "()))((()"]   # "()(())()"


for a in inputs:
    print(solution(a))



