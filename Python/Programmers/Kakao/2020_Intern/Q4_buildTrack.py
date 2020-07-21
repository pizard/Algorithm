# Rule
#   출발점, 도착점 : 0
#   항상 건설 가능한 형태로 나옴
#   종류
#       직선도로 : 상하 or 좌우 연결 (100원)
#       코너    : 직각으로 연결 (500원)

# Input
#   Board : 도면의 상태, 2차원 배열 (N x N)
#       length : 3 ~ 25
#       val : 0 or 1 (0 : 도로 연결 가능, 1 : 도로 연결 불가능)
# Output
#   건설 최소 비용

# locList
#   key : x, y, direction (List)b
#   value : payment (int)

import sys
sys.setrecursionlimit(100000)

def insertLoc(locList, loc, board, boardLength) -> bool:
    if (0 <= loc[0] and loc[0] < boardLength) and (0 <= loc[1] and loc[1] < boardLength): # board 내부
        if board[loc[0]][loc[1]] == 0: # 비어있는 곳
            if (loc[0], loc[1], loc[  2]) in locList.keys(): # 있는 경우
                if locList[(loc[0], loc[1], loc[2])] > loc[3]:
                    locList[(loc[0], loc[1], loc[2])] = loc[3]
                    mov(locList, loc, board, boardLength)
                else:
                    pass
            else: # 없는 경우
                if min(locList.get((loc[0], loc[1], 0),float('inf')), locList.get((loc[0], loc[1], 1), float('inf'))) + 500 > loc[3]:
                    locList[(loc[0], loc[1], loc[2])] = loc[3]
                    mov(locList, loc, board, boardLength)

def mov(locList, loc, board, boardLength): # mov
    if loc[2] == 0: # 좌우
        # 오른쪽
        insertLoc(locList, [loc[0]+1, loc[1], 0, loc[3]+100], board, boardLength)
        # 왼쪽
        insertLoc(locList, [loc[0]-1, loc[1], 0, loc[3]+100], board, boardLength)
    if loc[2] == 1: # 상하
        # 아래
        insertLoc(locList, [loc[0], loc[1]+1, 1, loc[3]+100], board, boardLength)
        # 위
        insertLoc(locList, [loc[0], loc[1]-1, 1, loc[3]+100], board, boardLength)
    if loc[2] == 0: # 좌우
        # 아래
        insertLoc(locList, [loc[0], loc[1]+1, 1, loc[3]+600], board, boardLength)
        # 위
        insertLoc(locList, [loc[0], loc[1]-1, 1, loc[3]+600], board, boardLength)
    if loc[2] == 1: # 상하
        # 오른쪽
        insertLoc(locList, [loc[0]+1, loc[1], 0, loc[3]+600], board, boardLength)
        # 왼쪽
        insertLoc(locList, [loc[0]-1, loc[1], 0, loc[3]+600], board, boardLength)

    if loc[2] == -1: # start
        # 오른쪽
        insertLoc(locList, [loc[0]+1, loc[1], 0, loc[3]+100], board, boardLength)
        # 아래
        insertLoc(locList, [loc[0], loc[1]+1, 1, loc[3]+100], board, boardLength)

def solution(board):
    boardLength = len(board)
    locList = {} # x, y, direction(-1: 전체, 0:좌우, 1:상하), payment
    mov(locList, [0,0,-1,0], board, boardLength)

    return min(locList.get((boardLength-1, boardLength-1, 0), float('inf')), locList.get((boardLength-1, boardLength-1, 1), float('inf')))


print(solution([[0,0,0],[0,0,0],[0,0,0]])) # 900

print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]])) # 3800

print(solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]])) # 2100