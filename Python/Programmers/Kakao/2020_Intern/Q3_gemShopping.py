#
# Input
#   gems : 진열대 번호 순서대로 보석들의 이름이 저장된 배열
# Output
#   모든 보석을 하나 이상 포함하는 가장 짧은 구간(시작 진열대 번호, 끝 진열대 번호)
#   여러개인경우 시작 진열대 번호가 가장 작은 구간 return


def solution(gems):
    gemList = set(gems)
    startIdx = 0
    gemCoverList = [gemList.copy() for x in range(len(gems))]
    answer = []

    for idx in range(len(gems)): # idx번째 보석
        startFlg = True
        for checkIdx in range(startIdx, idx+1): # idx 이전의 보석들에서 idx 보석 제거
            gemCoverList[checkIdx].discard(gems[idx])
            if len(gemCoverList[checkIdx]) == 0:
                if startFlg == True:
                    startIdx = checkIdx+1
                gemCoverList[checkIdx] = idx - checkIdx
            startFlg == False
            gemList.discard(idx)

    minCover = len(gems)
    for i in range(len(gemCoverList)):
        if type(gemCoverList[i]) == set:
            break;
        if minCover > gemCoverList[i]:
            answer = [i+1, i+gemCoverList[i]+1]
            minCover = gemCoverList[i]

    return answer



print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))

print(solution(["AA", "AB", "AC", "AA", "AC"]))

print(solution(["XYZ", "XYZ", "XYZ"]))

print(solution(["XYZ", "Xkk", "XY"]))
