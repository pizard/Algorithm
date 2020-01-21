'''
문제 설명
숫자 야구 게임이란 2명이 서로가 생각한 숫자를 맞추는 게임입니다.
각자 서로 다른 1~9까지 3자리 임의의 숫자를 정한 뒤 서로에게 3자리의 숫자를 불러서 결과를 확인합니다. 그리고 그 결과를 토대로 상대가 정한 숫자를 예상한 뒤 맞힙니다.
* 숫자는 맞지만, 위치가 틀렸을 때는 볼
* 숫자와 위치가 모두 맞을 때는 스트라이크
* 숫자와 위치가 모두 틀렸을 때는 아웃
예를 들어, 아래의 경우가 있으면

A : 123
B : 1스트라이크 1볼.
A : 356
B : 1스트라이크 0볼.
A : 327
B : 2스트라이크 0볼.
A : 489
B : 0스트라이크 1볼.
이때 가능한 답은 324와 328 두 가지입니다.

질문한 세 자리의 수, 스트라이크의 수, 볼의 수를 담은 2차원 배열 baseball이 매개변수로 주어질 때, 가능한 답의 개수를 return 하도록 solution 함수를 작성해주세요.

제한사항
질문의 수는 1 이상 100 이하의 자연수입니다.
baseball의 각 행은 [세 자리의 수, 스트라이크의 수, 볼의 수] 를 담고 있습니다.
'''

import itertools


# (QuestionNum, StrikeNum, BallNum) -> PossibleNum
# 1 ~ 9

# Idea 1
# 1. 모든 값 생성
# 2. 해당 값 확인하며 제

# Idea 2 -> 음....
# 1. strike -> ball 순으로 정렬
# 2. 첫 Game에서 가능한 모든 Value 생성
# 3. 제거해가며 진행


# Idea 3 -> 음.... ^~^
# 1. strike -> ball 순으로 정렬
# 2. 앞에서 부터 차례로 비교 해서... 핳..?




baseball = [[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]
def makeAnswerList(length, replication, notContainNums):
    answer = []
    startNum, endNum= 10**(length-1), 10**length

    for x in range(startNum, endNum):
        checkTemp = set(str(x))
        if replication == False:
            if len(checkTemp) != length:
                continue
        for notContainNum in notContainNums:
            if str(notContainNum) not in checkTemp:
                answer.append(x)
    return answer

def solution(baseball):
    # answers = makeAnswerList(3, False, [0])
    answers = list(itertools.permutations([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))
    for game in baseball:
        for answer in reversed(answers):
            if SBGame(game[0], answer) != game[1:]:
                answers.remove(answer)

    return len(answers)

def SBGame(throwNum, answerNum):
    S, B = 0, 0
    throwNumSplit, answerNumSplit = str(throwNum), str(answerNum)

    for digit in range(0, len(throwNumSplit)):
        if throwNumSplit[digit] == answerNumSplit[digit]:
            S += 1
        elif throwNumSplit[digit] in answerNumSplit:
            B += 1
    return [S, B]

print(solution(baseball))