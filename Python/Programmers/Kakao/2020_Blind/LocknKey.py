import copy
def solution(key, lock):
    N = len(lock)
    M = len(key)
    for i in range(0, 4):
        for x in range(-M+1, N):
            for y in range(-M+1, N):
                if (checkOpen(lock, moving(key, lock,x,y))):
                    return True
        rotationClock(key, 1)
    return False


def rotationClock(key, num):
    M = len(key)
    tempKey = copy.deepcopy(key)
    for i in range(0,num):
        for x in range(0, M):
            for y in range(0, M):
                key[y][M-x-1] = tempKey[x][y]

def moving(key, lock, right, down):
    N = len(lock)
    M = len(key)
    matrix = [[0 for col in range(N)] for row in range(N)]

    for h in range(0, N):
        for w in range(0, N):
            if down+h >= N or right+w >= N or down+h < 0 or right+w < 0:
                continue
            if h >= M or w >= M or h < 0 or w < 0:
                continue
            matrix[down+h][right+w] = key[h][w]
    return matrix


def checkOpen(lock, key):
    for x in range(0, len(lock)):
        for y in range(0, len(lock[0])):
            if lock[x][y]+key[x][y] == 0 or lock[x][y]+key[x][y] == 2:
                return False
    return True






def printArray(key):
    print("---------")
    for x in range(0, len(key)):
        print(key[x])
    print("---------")

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1, 1], [1, 1, 0, 1], [1, 0, 1, 1], [0, 1, 0, 1]]))