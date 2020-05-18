def solution(board):
    answer = 0



    return answer




class RobotState:
    def __init__(self, r, c, d, m): # r:row, c:column, d:direction, m:move
        self.r = r # row 위치     -> 무조건 작은 위치 기
        self.c = c # column 위치
        self.d = d # 방향, 0:right, 1:down
        self.m = m # 움직인 횟수

class BoardState:
    def __init__(self, board, stateList):
        self.board = board
        self.stateList = []

    def turning(self, insertState, direction):  # 0: Clockwise, 1 : CounterClockwise
        if direction == 0:
            if insertState.r + 1 < len(self.board) and self.board[insertState.r+1][insertState.c-1] != 1:
                self.insertState(RobotState(insertState.r , insertState.c, insertState.d, insertState.m + 1))

        #####
        # elif direction == 1:

        # else:

    def moving(self, direction):  # 0: Right, 1:Down / 2:Left, 3: Up
        return 0



    def insertState(self, insertState):
        if insertState.d == 2: # Left -> Right
            insertState.d = 0
            insertState.c -= 1
        elif insertState.d == 3: # Up -> Down
            insertState.d = 1
            insertState.r -= 1

        for state in self.stateList:
            if self.checkDuplicate(insertState, state):
                return True
        return False

    def checkDuplicate(self, insertState, state):
        if state.r == insertState.r and state.c == insertState.c and state.d == insertState.d: # 같은 경우
            if state.m > insertState.m: # 횟수 확인
                return True
        return False

    def checkFinish(self, state):
        length = len(self.board)
        if state.r == length-1 and state.c == length and state.d == 1: # 아래 방향
            return True
        elif state.r == length and  state.c == length-1 and state.d == 0: # 좌우 방향
            return True
        return False
