# Construct
#   원형, n미터

# Input
#   n    : 외벽의 길이 ( 1 ~ 200 )
#   weak : 취약 지점의 위치 ( 1 ~ 15 )
#       위치가 같은 경우는 없음
#       오름차순
#       val : 0 ~ n-1
#   dist : 각 친구들의 1시간 이동 가능 거리 ( 1 ~ 8 )
#       val : 1 ~ 100
# Output
#   점검을 보내는 친구 수의 최솟값
#   불가능한 경우 : -1

from itertools import permutations
def solution(n, weak, dist):
    # 1. dist 내림차순 정렬
    # 2. dist의 수를 1개씩 늘려가며 가능 여부 확인
    # 2-1. 모든 weak에 대해 검색

    dist.sort(reverse=True)
    for i in range(1, len(weak)+1):
        permutation = permutations(dist, i)
        for p in permutation:
            for start in range(len(weak)):
                _left = weak[:start]; _right = weak[start:]
                traverse_list = _right + [i+n for i in _left] # weak point
                candidate = list(p.copy())                    # 친구 커버 범위
                while traverse_list and candidate:
                    cur = traverse_list.pop(0) #
                    d = candidate.pop(0)
                    cover = cur + d
                    while traverse_list and traverse_list[0] <= cover:
                        traverse_list.pop(0)
                if not traverse_list:
                    return i

    return -1

print(solution(21, [1, 5, 6, 10], [1, 2, 3, 4])) #