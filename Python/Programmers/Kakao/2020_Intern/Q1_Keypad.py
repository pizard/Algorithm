# Rule
#   Start : L -> *, R -> #
#   1. 상하좌우 4가지 방향
#   2. 1,4,7 -> L
#   3. 3,6,9 -> R
#   4. 2, 5, 8, 0 -> 가까운 손가락, 같은 경우 주요 사용 손

# Input
#   numbers : 순서대로 누를 번호
#       size : 1 ~ 1000
#       val  : 0 ~ 9
#   hand : 오른손잡이 or 왼손잡이 (right or left)

# Output
#   각 번호를 누른 엄지손가락이 왼손 or 오른손 문자열 (L or R)

# 20분

def calDistance(loc1, loc2):
    return (abs(loc1[0]-loc2[0]) + abs(loc1[1]-loc2[1]))

def solution(numbers, hand):
    table = {   1  : [0,0], 2 : [0,1],  3  : [0,2]
             ,  4  : [1,0], 5 : [1,1],  6  : [1,2]
             ,  7  : [2,0], 8 : [2,1],  9  : [2,2]
             , "*" : [3,0], 0 : [3,1], "#" : [3,2]}

    L = "*"
    R = "#"
    mainHand = "R" if hand == "right" else "L"

    answer = ""
    for number in numbers:
        if number == 1 or number == 4 or number == 7:
            answer += "L"
            L = number
        elif number == 3 or number == 6 or number == 9:
            answer += "R"
            R = number
        else:
            if calDistance(table[number], table[L]) > calDistance(table[number], table[R]): # R
                answer += "R"
                R = number

            elif calDistance(table[number], table[L]) < calDistance(table[number], table[R]): # L
                answer += "L"
                L = number

            else: # Equal
                if mainHand == "R":
                    answer += "R"
                    R = number
                else:
                    answer += "L"
                    L = number

    return answer



print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right")) # "LRLLLRLLRRL"