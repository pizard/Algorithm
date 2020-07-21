# Rule
#   Start : Room 0
#   A -> B의 최단 경로는 오직 하나, 불가능한 경우는 없음
#   1. 모든 방은 적어도 1회 방문
#   2. 순서 결정되어 있음 (Order)
#       이전 방은 최대 1개
# Input
#   n       : 방의 갯수
#       val : 2 ~ 200,000
#   path    : 각 통로를 연결하는 두 방의 번호(2D array)
#       val : [Room A, Room B], A <-> B
#   order   : 프로도가 정한 방문 순서(2D array)
#       val : [Room A, Room B], A -> B
# Output
#   규칙에 맞게 모든 방을 탐헐할 수 있을지 (True or False)

# 그냥 한턴씩 출발하면 될 것 같은데..?
# 0 -> [1,3,7] ->



def roomValidation(roomDone, roomSearch, roomMap, searchRoomNum, childRoom):
    if childRoom not in roomDone and childRoom not in roomSearch:
        roomSearch.add(childRoom)
    else:
        roomMap[searchRoomNum].remove(childRoom)

def solution(n, paths, orders) -> bool:
    # 1. Tree 생성 (key : room, val : childNode
    roomDone = set() # 완료
    roomSearch = set([0]) # 검색 중
    roomMap = {i : [] for i in range(n)}
    roomOrder = {}
    for path in paths:
        roomMap[path[0]].append(path[1])
        roomMap[path[1]].append(path[0])
    for order in orders:
        roomOrder[order[0]] = order[1] # val -> key

    # 1. Search의 하위 Map -> Search
    #   1.1 Validation 확인 (Order)
    #   1.2 Searh에 있는 하위 Map 제거
    # 2. 모든 Search가 제거되면 Done 이동
    # 3. 위 과정들을 반복
    # 4. 2번을 해도 Search의 변화가 없는 경우 -> False
    # 5. 나온 경우 -> True

    while(len(roomDone) != n):
        roomSearchPrev = roomSearch.copy()
        for searchRoomNum in roomSearch.copy():
            for childRoom in roomMap[searchRoomNum].copy():
                # 1. Search의 하위 Map -> Search
                if childRoom in roomOrder.values(): # 우선 순위 조건이 걸린 경우
                    pass
                else: # 우선순위 조건이 안 걸린 경우
                    if childRoom in roomOrder.keys():
                        roomOrder.pop(childRoom)

                    # while(childRoom in roomOrder.keys()):
                    #     nextRoomNum = roomOrder[childRoom]
                    #     roomOrder.pop(childRoom)
                    #     childRoom = nextRoomNum
                    roomValidation(roomDone, roomSearch, roomMap, searchRoomNum, childRoom)

                    if len(roomMap[searchRoomNum]) == 0:
                        roomMap.pop(searchRoomNum)
                        roomSearch.remove(searchRoomNum)
                        roomDone.add(searchRoomNum)
        if roomSearchPrev == roomSearch:
            return False
    return True


solution(9, [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]], [[8,5],[6,7],[4,1]]) # true
solution(9, [[8,1],[0,1],[1,2],[0,7],[4,7],[0,3],[7,5],[3,6]], [[4,1],[5,2]]) # true
solution(9, [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]], [[4,1],[8,7],[6,5]]) # false