# Input
#   Treasure Box
#      각 변에 16진수 숫자(0~F)가 적혀있음
#      시계방향으로 회전 가능
#      시계 방향 순으로 높은 자리 숫자에 해당
#   Password
#      보물 상자에 적힌 숫자로 만들 수 있는 모든 수 중 K번째 수를 10진수로 변환한 값

# Constraint
#   N
#       val : 0 ~ F
#       len : 8 ~ 28, 4의 배

import sys

sys.stdin = open("input.txt", "r")


def decimalToHex(number, reverse = False):
    if reverse: return int("0x" + str(number), 16)   # 16 -> 10
    else: return hex(int(number))[2:]           # 10 -> 16

T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split(" "))
    treasureBox = (input())
    treasureBox *= 2
    N1, N2, N3, N4 = 0, 0, 0, 0

    length = N//4
    treasureValue = set()
    for i in range(0, 4):
        N1 = treasureBox[i+length * 0: i+length * 1]
        N2 = treasureBox[i+length * 1: i+length * 2]
        N3 = treasureBox[i+length * 2: i+length * 3]
        N4 = treasureBox[i+length * 3: i+length * 4]
        treasureValue.add(decimalToHex(N1,True))
        treasureValue.add(decimalToHex(N2,True))
        treasureValue.add(decimalToHex(N3,True))
        treasureValue.add(decimalToHex(N4,True))
    sortedTreasureValue = sorted(list(treasureValue), reverse=True)


    print('#{} {}'.format(test_case, sortedTreasureValue[K-1]))


