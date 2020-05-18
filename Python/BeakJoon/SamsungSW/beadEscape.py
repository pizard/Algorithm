# Board   -> 가로 : M, 세로 : N, 구멍 1개
# Bead    -> 빨간, 파란
# Purpose -> 빨간색 구슬 꺼내기, 중력 이동(위,아래,좌,우)
# Return  -> 최소 몇 번만에 구슬을 꺼낼 수 있는가?

# Input
# 3 <= N, M <= 10
# . : 빈 칸, # : 장애물, 0 : 구멍, R : Red Bead, B : Blue Bead
# 가장자리 : #,  0,R,B : 1개씩

from sys import stdin



class boardState():
    def __init__(self, board, red_row = -1, red_column = -1, blue_row = -1 , blue_column = -1):
        self.board = board
        self.count = 0

        if red_row != -1:
            self.red_row = red_row
            self.red_column = red_column
            self.blue_row = blue_row
            self.blue_column = blue_column
        else:
            for i, board_row in enumerate(board):
                for j, board_value in enumerate(board_row):
                    if board_value == "R":
                        self.red_row = i
                        self.red_column = j
                    if board_value == "B":
                        self.blue_row = i
                        self.blue_column = j

    def lean(self, direction): # 0:up, 1:right, 2:down, 3:left
        self.count += 1
        if direction == 0:


            for i in range(self.red_column, 0):
                if board[self.red_row][i] == ".":
                    red_column_new = i
                else:
                    if self.checkTheBlock(board[self.red_row][i]):
                        return self.count
                    else:
                        break;


        # elif direction == 1:
        #
        # elif direction == 2:
        #
        # elif direction == 3:

    def checkTheBlock(self, block):
        if block == "#" or block =="R" or block =="B":
            return False
        elif block == "0":
            return True


if __name__ == "__main__":
    input = stdin.readline()
    n, m = map(int, input().split())
    board = [list(input().strip()) for _ in range(n)]

    boardstate = boardState(board)



