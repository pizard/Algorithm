# Rule
#   초기 위치 (1,1) - (1,2)
#   이동 상, 하, 좌, 우, 회전
#
# Input
#   board : 0,1로 이루어진 지도
#       size : 5 ~ 100
#       val  : 0 or 1 (0:빈칸, 1:벽)
#
# Output
#   (N,N)까지 이동하는데 필요한 최소 시간


import sys
sys.setrecursionlimit(100000)

def move(board, robotLocList, robotLoc, movNum) -> int: # board : 전체 판, robotLocList : 로봇의 위치들, robotLoc : 현재 위치, movNum : 이동 횟수
    n = len(board)
    if (robotLoc[0] == n-1 and robotLoc[1] == n-1)\
        or (robotLoc[2] == n-1 and robotLoc[3] == n-1):
            if "answer" not in robotLocList.keys():
                robotLocList["answer"] = movNum-1
            elif robotLocList["answer"] > movNum-1:
                robotLocList["answer"] = movNum-1

    # 1. 아래
    movLoc = makeShape(robotLoc[0]+1, robotLoc[1], robotLoc[2]+1, robotLoc[3])
    if validationBoard(board, movLoc):
        if validationRobotLoc(robotLocList, movLoc, movNum):
            move(board, robotLocList, movLoc, movNum+1)
        if robotLoc[0] == robotLoc[2]:  # 가로형
            # 5. 회전 (왼쪽 기준, +90)
            movLoc = makeShape(robotLoc[0], robotLoc[1], robotLoc[2] + 1, robotLoc[3] - 1)
            if validationBoard(board, movLoc):
                if validationRobotLoc(robotLocList, movLoc, movNum):
                    move(board, robotLocList, movLoc, movNum + 1)
            # 8. 회전 (오른쪽 기준, -90)
            movLoc = makeShape(robotLoc[0] + 1, robotLoc[1] + 1, robotLoc[2], robotLoc[3])
            if validationBoard(board, movLoc):
                if validationRobotLoc(robotLocList, movLoc, movNum):
                    move(board, robotLocList, movLoc, movNum + 1)

    # 2. 위
    movLoc = makeShape(robotLoc[0]-1, robotLoc[1], robotLoc[2]-1, robotLoc[3])
    if validationBoard(board, movLoc):
        if validationRobotLoc(robotLocList, movLoc, movNum):
            move(board, robotLocList, movLoc, movNum+1)
        if robotLoc[0] == robotLoc[2]:  # 가로형
            # 7. 회전 (오른쪽 기준, +90)
            movLoc = makeShape(robotLoc[0]-1,robotLoc[1]+1,robotLoc[2],robotLoc[3])
            if validationBoard(board, movLoc):
                if validationRobotLoc(robotLocList, movLoc, movNum):
                    move(board, robotLocList, movLoc, movNum+1)
            # 6. 회전 (왼쪽 기준, -90)
            movLoc = makeShape(robotLoc[0],robotLoc[1],robotLoc[2]-1,robotLoc[3]-1)
            if validationBoard(board, movLoc):
                if validationRobotLoc(robotLocList, movLoc, movNum):
                    move(board, robotLocList, movLoc, movNum+1)

    # 3. 좌
    movLoc = makeShape(robotLoc[0], robotLoc[1]-1, robotLoc[2], robotLoc[3]-1)
    if validationBoard(board, movLoc):
        if validationRobotLoc(robotLocList, movLoc, movNum):
            move(board, robotLocList, movLoc, movNum+1)
        if robotLoc[1] == robotLoc[3]:  # 세로 & 왼쪽
            # 5. 회전 (왼쪽 기준, +90)
            movLoc = makeShape(robotLoc[0], robotLoc[1], robotLoc[2] - 1, robotLoc[3] - 1)
            if validationBoard(board, movLoc):
                if validationRobotLoc(robotLocList, movLoc, movNum):
                    move(board, robotLocList, movLoc, movNum + 1)
            # 8. 회전 (오른쪽 기준, -90)
            movLoc = makeShape(robotLoc[0] + 1, robotLoc[1] - 1, robotLoc[2], robotLoc[3])
            if validationBoard(board, movLoc):
                if validationRobotLoc(robotLocList, movLoc, movNum):
                    move(board, robotLocList, movLoc, movNum + 1)

    # 4. 우
    movLoc = makeShape(robotLoc[0], robotLoc[1]+1, robotLoc[2], robotLoc[3]+1)
    if validationBoard(board, movLoc):
        if validationRobotLoc(robotLocList, movLoc, movNum):
            move(board, robotLocList, movLoc, movNum+1)
        if robotLoc[1] == robotLoc[3]:  # 세로 & 오른쪽
            # 7. 회전 (오른쪽 기준, +90)
            movLoc = makeShape(robotLoc[0]+1,robotLoc[1]+1,robotLoc[2],robotLoc[3])
            if validationBoard(board, movLoc):
                if validationRobotLoc(robotLocList, movLoc, movNum):
                    move(board, robotLocList, movLoc, movNum+1)
            # 6. 회전 (왼쪽 기준, -90)
            movLoc = makeShape(robotLoc[0],robotLoc[1],robotLoc[2]-1,robotLoc[3]+1)
            if validationBoard(board, movLoc):
                if validationRobotLoc(robotLocList, movLoc, movNum):
                    move(board, robotLocList, movLoc, movNum+1)


def validationBoard(board, robotLoc) -> bool:
    n = len(board)
    if (0 <= robotLoc[0] and robotLoc[0]<n)\
        and (0 <= robotLoc[1] and robotLoc[1]<n)\
        and (0 <= robotLoc[2] and robotLoc[2]<n)\
        and (0 <= robotLoc[3] and robotLoc[3]<n):
        if board[robotLoc[0]][robotLoc[1]] == 0 and board[robotLoc[2]][robotLoc[3]] == 0:
            return True
    return False

def makeShape(x1,y1, x2, y2):
    if (x1 > x2) or (y1 > y2):
        return (x2, y2, x1, y1)
    return (x1, y1, x2, y2)

def validationRobotLoc(robotLocList, robotLoc, movNum) -> bool:
    if robotLoc not in robotLocList.keys():
        robotLocList[robotLoc] = movNum
        return True
    else:
        if robotLocList[robotLoc] > movNum:
            robotLocList[robotLoc] = movNum
            return True
    return False

def solution(board):
    # 1. 로봇 이동 (complete search))
    # 2. board 확인
    # 2-1. 가능 -> 3으로 이동
    # 2-2. 불가능 -> 삭제
    # 3. 기존 robot과의 비교
    # 3-1. robot.val < 이동 횟수 -> 교체 & 1로 이동
    # 3-2. robot.val > 이동 횟수 -> 삭제
    # 4. (n,n) 도달 : return
    robotLocList = {}  # dict, key : 위치, value : 이동 횟수
                       # key :tuple(x1,x2,x3,x4)
    start = (0,0,0,1)
    robotLocList[start] = 0
    move(board, robotLocList, start, 1)

    return robotLocList["answer"]


print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]])) # 7
print(solution([[0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1, 1], [0, 0, 1, 0, 0, 0, 0]])) # 21
print(solution([[0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0, 0]])) # 11
print(solution([[0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 0]])) # 33
