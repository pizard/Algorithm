# Input
#   1. board : 게임화면 (NxN, 5 ~ 30)
#       val : 0 ~ 100 (0 : 빈 칸)
#   2. moves : 작동 위치 (1 ~ 1000)
#       val : 1 ~
# Output
#   사라진 인형의 갯수

# Constraint
#   1. 바구니
#       크기 : 무제한
#       같은 모양 2개 -> 사라짐

def solution(board, moves):
    answer = 0
    basketStack = []
    boardStack = [[] for col in range(len(board))]

    for i in range(len(board)):
        for j in range(len(board)):
            # if board[len(board)-1-j][i] != 0: boardStack[i].append(board[len(board)-1-j][i])
            if board[j][i] != 0: boardStack[i].insert(0,board[j][i])
    for move in moves:
        if len(boardStack[move-1]) != 0:
            if len(basketStack) == 0 or basketStack[-1] != boardStack[move-1][-1]:
                basketStack.append(boardStack[move-1].pop())
            else:
                basketStack.pop()
                boardStack[move-1].pop()
                answer += 2


    return answer

# 4 -> 3 -> 1 -> 1 -> 3 -> 2 -> x -> 4
print(solution([[0,0,0,0,0]
         ,[0,0,1,0,3]
         ,[0,2,5,0,1]
         ,[4,2,4,4,2]
         ,[3,5,1,3,1]]
        ,[1,5,3,5,1,2,1,4]))