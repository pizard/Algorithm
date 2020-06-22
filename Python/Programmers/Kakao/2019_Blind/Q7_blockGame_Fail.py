# Board : N x N
# Constraint
#   1. Board : Block이 들어있는 NxN 배열 (N : 4 ~ 50)
#       원소 : 0 ~ 200 (0 : 빈칸, # : block)
#   2. 맵을 벗어날 수 없음
#   3. 속이 꽉 찬 직 사각형을 만들면 제거


def solution(board):
    onOff = [True] * len(board) # 해당 서치 필요 여부
    colBoard = [[] for row in range(len(board))]
    # 1. 저장
    blockDict = []
    for i in range(0, len(board)):
        for j in range(0, len(board)):
            colBoard[i].append(board[j][i])


    answer = 0
    return answer


solution([[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,4,0,0,0],[0,0,0,0,0,4,4,0,0,0],[0,0,0,0,3,0,4,0,0,0],[0,0,0,2,3,0,0,0,5,5],[1,2,2,2,3,3,0,0,0,5],[1,1,1,0,0,0,0,0,0,5]])