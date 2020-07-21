# 수식 최대화 : 1시간 5분...ㅜㅜ
# Rule
#   연산자의 우선 순위를 재정의 하여 최대 값 출력
#   같은 순위의 연산자는 없
#   같은 연산자 -> 앞이 우선순위
#   결과 값 음수 -> 절대 값 사용
# Input
#   expression : 연산 수식이 담긴 문자열
#       size : 3 ~ 100
#       val :하
#          연산자  : +, -, *, 중위표기법
#          피연산자 : 0 ~ 999
# Output
#   우승 시 받을 수 있는 가장 큰 상금 금액
#   2^63-1 이하



import re
from itertools import permutations
def calcul(num1, num2, oper):
    if oper =="+":
        return num1 + num2
    elif oper == "*":
        return num1 * num2
    elif oper == "-":
        return num1 - num2

    return "Error"
def solution(expression):
    answer = 0
    operatorList = re.compile("[^0-9]").findall(expression) # 연산
    operandList = [int(n) for n in re.split("[*+-]",expression)] # 숫자

    operatorPriorityCandidates = permutations(set(operatorList))

    maxResult = 0
    for operatorPriorityCandidate in operatorPriorityCandidates:
        tempOperatorList = operatorList.copy()
        tempOperandList = operandList.copy()
        for operatorPriority in operatorPriorityCandidate:
            # for i, operator in enumerate(tempOperatorList):
            idx = 0
            while idx < len(tempOperatorList):
                operator = tempOperatorList[idx]
                if operator == operatorPriority:
                    tempOperandList.insert(idx,calcul(tempOperandList[idx], tempOperandList[idx+1], operator))
                    tempOperandList.pop(idx+1)
                    tempOperandList.pop(idx+1)
                    tempOperatorList.pop(idx)
                else:
                    idx +=1

        if maxResult < abs(tempOperandList[0]):
            maxResult = abs(tempOperandList[0])
    return maxResult



solution("100-200*300-500+20") # 60420
# solution("100+200+300+400+500+600+700") # 2800