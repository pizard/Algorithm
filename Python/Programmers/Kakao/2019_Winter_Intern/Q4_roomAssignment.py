# Input
#   k : 방 갯수 (1 ~ 10^12)
#   room_number : 원하는 방 번호
#       size : 1 ~ 200,000
#       val  : 1 ~ k
# Constraint
#   1. Rule
#       1. 한 번에 한 명씩 신청한 순서대로 방을 배정합니다.
#       2. 고객은 투숙하기 원하는 방 번호를 제출합니다.
#       3. 고객이 원하는 방이 비어 있다면 즉시 배정합니다.
#       4. 고객이 원하는 방이 이미 배정되어 있으면 원하는 방보다 번호가 크면서 비어있는 방 중 가장 번호가 작은 방을 배정합니다.
# Output

def binary_search(target, data, sort = False):
    if not sort:
        data.sort()
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2

        if data[mid] == target:
            return mid # 함수를 끝내버린다.
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid -1

    while data[mid] < target:
        mid += 1

    return mid


def solution(k, room_numbers):
    answer = []
    roomList = list(range(1, k+1))

    for room_number in room_numbers:
        answer.append(roomList.pop(binary_search(room_number,roomList, True)))
    return answer


solution(10, [1,3,4,1,3,1])
