
# Constraint
#   1. 닉네임 변경 시 기존의 내용들 함께 변경
#   2. 중복 닉네임 허용
#   3. 닉네임 변경 규칙
#      3-1. 나간 후 다시 들어옴
#      3-2. 채팅방에서 변경

# Input
#   record : 닉네임 변경 기록
#       [Type, UserId, NickName]

# Output
#   최종 메시지 문자열

def solution(record):
    answer = []
    nickName = {}

    for value in record:
        val = value.split(" ")
        if val[0] == "Change" or val[0] == "Enter":
            nickName[val[1]] = val[2]
        else:
            if val[1] not in nickName.keys():
                nickName[val[1]] = val[2]

    for value in record:
        val = value.split(" ")

        if val[0] !="Change":
            if val[0] == "Enter":
                val[0] = "님이 들어왔습니다."
            elif val[0] == "Leave":
                val[0] = "님이 나갔습니다."
            answer.append(nickName[val[1]] + val[0])
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))