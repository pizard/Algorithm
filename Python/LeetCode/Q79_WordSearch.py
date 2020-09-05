import copy
class Solution:
    def exist(self, board , word: str) -> bool:
        self.board = board
        self.boardX = len(board)
        self.boardY = len(board[0])
        boardCheck = [[True for _ in range(0, self.boardY)] for _ in range(0, self.boardX)]

        self.answer = False


        for i in range(0, self.boardX):
            for j in range(0, self.boardY):
                if board[i][j] == word[0]:
                    boardCheckTemp = copy.deepcopy(boardCheck)
                    boardCheckTemp[i][j] = False
                    self.search(boardCheckTemp, i, j, word[1:])
        return self.answer
    # prev :  0: 위, 1:오른, 2:아래, 3:좌
    def search(self, boardCheck, locX, locY, remain):
        if remain == "":
            self.answer = True
            return
        if self.validation(boardCheck, locX-1, locY, remain[0]):
            boardCheckTemp = copy.deepcopy(boardCheck)
            boardCheckTemp[locX-1][locY] = False
            self.search(boardCheckTemp, locX-1, locY, remain[1:])
        if self.validation(boardCheck, locX, locY+1, remain[0]):
            boardCheckTemp = copy.deepcopy(boardCheck)
            boardCheckTemp[locX][locY+1] = False
            self.search(boardCheckTemp, locX, locY+1, remain[1:])
        if self.validation(boardCheck, locX+1, locY, remain[0]):
            boardCheckTemp = copy.deepcopy(boardCheck)
            boardCheckTemp[locX+1][locY] = False
            self.search(boardCheckTemp, locX+1, locY, remain[1:])
        if self.validation(boardCheck, locX, locY-1, remain[0]):
            boardCheckTemp = copy.deepcopy(boardCheck)
            boardCheckTemp[locX][locY-1] = False
            self.search(boardCheckTemp, locX, locY-1, remain[1:])
        return
    def validation(self, boardCheck, locX, locY, check):
        if (not (locX < 0 or locX >= self.boardX or locY < 0 or locY >= self.boardY))\
                and self.board[locX][locY] == check\
                and boardCheck[locX][locY] == True:
            return True
        return False

sol = Solution()
print(sol.exist([
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
    ], "ABCCED"))

print(sol.exist([["A","B","C","E"]
                ,["S","F","E","S"]
                ,["A","D","E","E"]], "ABCEFSADEESE"))