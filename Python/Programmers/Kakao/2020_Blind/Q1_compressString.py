# Rule
#   aabbaccc -> 2a2ba3c
#   ababcdcdababcdcd -> ababcdcd2
#   ...
# Input
#   s : 문자열 (1 ~ 1000)
#     val : 알파벳 소문
# Output
#   문자열을 잘라 표현한 문자열 중 가장 짧은 것의 길이


def solution(s):
    length = len(s)
    splitStrings = [[] for i in range(0, length//2 + 1)]
    for i in range(1, length//2 + 1):
        divider = 0
        while True:
            if divider < length:
                if divider + i > length:
                    pass
                    splitStrings[i].append(s[divider:length])  # 이번에 잘린 값
                else:
                    pass
                    splitStrings[i].append(s[divider:divider+i]) # 이번에 잘린 값
            else:
                # print(splitStrings[i])
                break;
            divider += i

    answer = len(s)
    splitStrings.pop(0)
    for splitString in splitStrings:
        compressString = ""
        prevString = ""
        duplicateNum = 1
        breakPoint = False
        while True:
            if len(splitString) > 0: # val이 있는 경우
                curString = splitString.pop(0)
            else:
                curString = ""
                breakPoint = True

            if prevString == curString:
                duplicateNum += 1
            else:
                compressString += prevString
                if duplicateNum != 1:
                    compressString += str(duplicateNum)
                duplicateNum = 1
            if breakPoint:
                break
            prevString = curString
        if len(compressString) < answer:
            answer = len(compressString)

    return answer





print(solution("xababcdcdababcdcd")) # 17