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
    answer = 0
    sortedStones = list(set(sorted(stones)))
    start = 0
    end = len(sortedStones)-1
    successNum = 0
    failNum = 0
    while start <= end:
        mid = (end+start) // 2
        if steppingStones(stones, sortedStones[mid], k):
            # 성공
            start = mid + 1
            successNum = sortedStones[mid]
        else:
            # 실패
            end = mid - 1
            failNum = sortedStones[mid]
    if failNum == 0:
        answer = successNum
    else:
        start = successNum
        end = failNum
        while start <= end:
            mid = (end+start) // 2
            if steppingStones(stones, mid, k):
                # 성공
                start = mid + 1
                answer = mid
            else:
                # 실패
                end = mid - 1

    return answer

# 건널 수 있는가 없는가?
def steppingStones(stones, Num, k) -> bool: # stones : 돌, Num : 인원, k : 최대 칸 수
    emptyLen = 0
    for stone in stones:
        if stone < Num:
            emptyLen += 1
        else:
            if emptyLen >= k:
                return False
            emptyLen = 0
    if emptyLen >= k:
        return False
    return True


# print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))
print(solution([3,3,3,3,3], 3))

