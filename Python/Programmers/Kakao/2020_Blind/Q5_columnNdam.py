# Rule
#   Column(기둥)
#       설치 조건 : 바닥 위, 보의 한쪽 끝, 다른 기둥 위
#       설치 방향 : 위쪽
#   Dam(보)
#       설치 조건 : 한 쪽 끝부분이 기둥 위, 양쪽 끝 부분이 다른 보와 동시에 연결
#                 바닥 설치 불가
#       설치 방향 : 오른쪽
#   공통
#       벽면에 벗어나게 기둥 or 보 설치 불가능
#       규칙에 맞지 않는 경우 해당 작업 무시
#       삭제 후에도 남은 기둥과 보 또한 규칙을 만족해야함
#
#
# Input
#   n : 벽면의 크기
#       size : 5 ~ 100
#   build_frame : 기둥과 보를 설치하거나 삭제하는 작업이 담겨 있음
#       [x, y, a, b]로 구성된 2차원 배
#           x, y : 기둥, 보를 설치 또는 삭제할 교차점의 좌표 (가로, 세로)
#           a : 구조물의 종류 (0 : col, 1 : dam)
#           b : 설치 or 삭제 여부 ( 0 : 삭제, 1 : 설치)
# Output : 최종 구조물의 상태
#   [x, y, a]로 구성된 2차원 배열
#       x, y : 기둥, 보의 교차점 좌표 (가로, 세로)
#       a :구조물의 종류(0 : 기둥, 1 : 보)
#   x좌표 -> y좌표 -> 종류(기둥 > 보) 오름차순 정렬


# [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
def solution(n, build_frames):
    board = [[[] for row in range(0, n+1)] for col in range(0, n+1)]
    for build_frame in build_frames:                       # 0 : 기둥, 1 : 보
        if build_frame[2] == 0 and build_frame[3] == 0:    # col & delete
            deleteValidationCheck(board, build_frame)
        elif build_frame[2] == 1 and build_frame[3] == 0:  # dam & delete
            deleteValidationCheck(board, build_frame)
        elif build_frame[2] == 0 and build_frame[3] == 1:  # col & install
            installValidationCheck(board, build_frame)
        elif build_frame[2] == 1 and build_frame[3] == 1:  # dam & install
            installValidationCheck(board, build_frame)

    answer = []
    for col in range(0, n+1):
        for row in range(0, n+1):
            if 0 in board[col][row]:
                answer.append([col,row,0])
            if 1 in board[col][row]:
                answer.append([col,row,1])
    return answer



def installValidationCheck(board, build_frame) -> bool:
    result = False
    if build_frame[2] == 0 and build_frame[3] == 1:  # col & install
        if build_frame[1] == len(board): # 가장 위
            result = False
        elif build_frame[1] == 0: # 바닥 위
            result = True
        elif 1 in board[build_frame[0]-1][build_frame[1]]\
            or 1 in board[build_frame[0]][build_frame[1]]: # 보의 한쪽 끝
                result = True
        elif 0 in board[build_frame[0]][build_frame[1]-1]: # 다른 기둥 위
            result = True
    if build_frame[2] == 1 and build_frame[3] == 1: # dam & install
        if build_frame[0] == len(board): # 오른쪽 끝
            result = False
        elif build_frame[1] == 0: # 바닥 위
            result = False
        elif 0 in board[build_frame[0]][build_frame[1]-1]\
            or 0 in board[build_frame[0]+1][build_frame[1]-1]: # 한쪽 끝 부분 기둥 위
            result = True
        elif 1 in board[build_frame[0]-1][build_frame[1]]\
            and 1 in board[build_frame[0]+1][build_frame[1]]: # 양쪽 보
            result = True

    if result:
        board[build_frame[0]][build_frame[1]].append(build_frame[2])
    return result



import copy
def deleteValidationCheck(board, build_frame):
    boardTemp = deleteConstruct(board, build_frame)
    # if build_frame[2] == 0: # col
    #     for build in boardTemp[build_frame[0]][build_frame[1]]
    # elif build_frame[2] == 1: # dam

def deleteConstruct(board, build_frame):
    temp = copy.deepcopy(board)
    temp[build_frame[0]][build_frame[1]].remove(build_frame[2])
    return temp

# Rule
#   Column(기둥)
#       설치 조건 : 바닥 위
#                 보의 한쪽 끝
#                 다른 기둥 위
#       설치 방향 : 위쪽
#   Dam(보)
#       설치 조건 : 바닥 위 X
#                 한 쪽 끝부분이 기둥 위
#                 양쪽 끝 부분이 다른 보와 동시에 연결
#       설치 방향 : 오른쪽
#   공통
#       벽면에 벗어나게 기둥 or 보 설치 불가능
#       규칙에 맞지 않는 경우 해당 작업 무시
#       삭제 후에도 남은 기둥과 보 또한 규칙을 만족해야함
# print(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))
# [[1,0,0],[1,1,1],[2,1,0],[2,2,1],[3,2,1],[4,2,1],[5,0,0],[5,1,0]]

print(solution(5, [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]))
# [[0, 0, 0], [0, 1, 1], [1, 1, 1], [2, 1, 1], [3, 1, 1], [4, 0, 0]]

