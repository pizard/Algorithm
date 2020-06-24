# Constraints
#   친구의 수 무제한

# Input
#    stones : 징검다리
#       size : 1 ~ 200,000
#       val  : 1 ~ 200,000,000
#    k : 한 번에 건너뛸 수 있는 디딤돌의 최대 칸
#       val : 1 ~ len
# Output
#    최대 몇 명까지 건널 수 있는지


def solution(stones, k):
    sortedStones = sorted(stones, key=lambda x : x)
    fail = 0

    passIndex = k
    prevPassNum = -1
    while True:
        passNum = sortedStones[passIndex]
        if prevPassNum != passNum:
            for stone in stones:
                if stone <= passNum:
                    fail += 1
                else:
                    if fail >= k:
                        return passNum
                    fail = 0
        passIndex += 1
        prevPassNum = passNum
    return passNum

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))

# 0, 1, 2, 0, 0, 0, 1, 0, 2, 0