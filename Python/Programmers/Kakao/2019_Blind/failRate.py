# FailRate : 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
# Input
#   N : # of Stages
#   stages : # of user who stopped in that stage
# Return
#   descend failrate
# Constract
#              N : 1 ~ 500
#         stages : 1 ~ 200,000
#   stages value : 1 ~ N+1 (N+1 : 마지막 스테이지까지 클리어)
# 만약 실패율이 같은 스테이지가 있다면 작은 번호 우선
# 해당 스테이지에 도달한 유저가 없는 경우 실패율 : 0




def solution(N, stages):
    answer = []
    # 1. Dict 형으로 key, value
    list = [0] * (N+2) # 0, N, all clear
    for stage in stages:
        list[stage] += 1

    failRate = [0] * (N+2)
    valueSum = 0
    for i in range(N+1, 0, -1): # N+1 ~ 0
        valueSum += list[i]
        if valueSum == 0:
            failRate[i] = 0
        else:
            failRate[i] = list[i]/valueSum
    failRate = failRate[1:N+1]

    return sorted(range(1,N+1), key=lambda k: failRate[k-1], reverse=True)

# 	[3,4,2,1,5]
# solution(5, [2, 1, 2, 6, 2, 4, 3, 3])
print(solution(4, [4,4,4,4,4]))


