# Construct
#   원형, n미터


# Input
#   n    : 외벽의 길이 ( 1 ~ 200 )
#   weak : 취약 지점의 위치 ( 1 ~ 15 )
#       위치가 같은 경우는 없음
#       오름차순
#       val : 0 ~ n-1
#   dist : 각 친구들의 1시간 이동 가능 거리 ( 1 ~ 8)
#       val : 1 ~ 100
# Output
#   점검을 보내는 친구 수의 최솟값
#   불가능한 경우 : -1

from itertools import permutations
def solution(n, weaks, dists):
    answer = 13

    candidates = list(permutations(dists))
    weaks += [weak+n for weak in weaks]
    weaksCycle = weaks + [weakCycle+n for weakCycle in weaks]
    for candidate in candidates:
        for i in range(0, len(weaks)):
            candidateIdx = 0
            weakStartIdx = i
            weakEndIdx = i+1
            answerTemp = 0
            checkIter = True
            while checkIter:
                if weaksCycle[weakEndIdx] - weaksCycle[weakStartIdx] > candidate[candidateIdx]:
                    # 커버를 못 하는 경우
                    if weakEndIdx - weakStartIdx == 1:
                        checkIter = False
                        break
                    candidateIdx += 1
                    weakStartIdx = weakEndIdx
                    answerTemp += 1
                else:
                    pass
                # pass
                weakEndIdx += 1
                if weakEndIdx == i + len(weaks): # 보수를 끝낸 경우
                    answerTemp += 1
                    break;
                if candidateIdx == len(candidate):
                    checkIter = False

            if checkIter and (answer > answerTemp):
                answer = answerTemp
    return -1 if answer == 13 else answer

print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4])) #



"""
    weakDists = [[] for col in range(0, len(weaks))]
    length = len(weaks)
    weaks += [weak+n for weak in weaks]
    for start in range(length):
        if start == 0:
            previous = - (n - weaks[length-1])
        else:
            previous = weaks[start-1]
    
        for i in range(start, start+length):
            weakDists[start].append(weaks[i]-previous)
            previous = weaks[i]
"""