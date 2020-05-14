'''
https://programmers.co.kr/learn/courses/30/lessons/42747

문제 설명
H-Index는 과학자의 생산성과 영향력을 나타내는 지표입니다. 어느 과학자의 H-Index를 나타내는 값인 h를 구하려고 합니다. 위키백과1에 따르면, H-Index는 다음과 같이 구합니다.

어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h가 이 과학자의 H-Index입니다.
어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때, 이 과학자의 H-Index를 return 하도록 solution 함수를 작성해주세요.

제한사항
과학자가 발표한 논문의 수는 1편 이상 1,000편 이하입니다.
논문별 인용 횟수는 0회 이상 10,000회 이하입니다.
'''


# Idea3 : Binary Search.py
# 논문 갯수 : PaperNum, 인용 횟수 : QuoteNum
# Control -> PaperNum
# 1. PaperNum & QuoteNum 비교
# 2-1. PaperNum > QuoteNum : (↓ : no need, ↑ : check need)  [0, 1, 2, 5, 6]
# 2-1. PaperNum = QuoteNum : (↓ : no need, ↑ : check need)  [0, 1, 3, 5 ,6]
# 2-2. PaperNum < QuoteNum : (↓ : check need, ↑ : no need)  [0, 2, 4, 5, 6]

# H-Index
# PaperNum >= h
# QuoteNum >= h


# Example

# citations = [6, 6, 6, 6, 6, 6, 10]
# Index          : 1, 2, 3, 4, 5, 6, 7
# PaperNum       : 7, 6, 5, 4, 3, 2, 1
# QuoteNum (2-1) : 0, 1, 2, 3, 3, 5, 6
# QuoteNum (2-1) : 0, 1, 3, 4, 4, 5, 6
# QuoteNum (2-2) : 0, 1, 4, 5, 5, 5, 6

# Quote : 0, 0, 1
# Paper : 3, 2, 1

# 7, 6, 5, 4, 3, 2, 1
# 6, 6, 6, 6, 6, 6, 10
# 0이상인게 3개
#

def solution(citations):
    answer = 0
    citations.sort()

    start = 0
    end = len(citations) - 1

    while start <= end:
        checkLocation = (start + end) // 2
        paperNum = len(citations) - checkLocation
        quoteNum = citations[checkLocation]

        # 2-1. PaperNum > QuoteNum : (Index : ↓X, ↑O)
        # 2-1. PaperNum = QuoteNum : (Index : ↓X, ↑O)
        if paperNum >= quoteNum:
            start = checkLocation+1
            if answer < min(paperNum, quoteNum):
                answer = min(paperNum, quoteNum)

        # 2-2. PaperNum < QuoteNum : (Index : ↓O, ↑X)
        elif paperNum < quoteNum:
            end = checkLocation-1
            if answer < paperNum:
                answer = paperNum

#        print("(PaperNum, quoteNum) : (", paperNum, ", ", quoteNum,  "), answer : ", answer)

    return answer