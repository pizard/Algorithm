# 불량 사용자, 제재 아이디 : 당첨 제외자
# Constraint
#   * : 1개 이상
# Input
#   user_id : 응모자 아이디 목록 (List)
#       size : 1 ~ 8
#       length : 1 ~ 8
#       중복 x, 알파벳 소문자 & 숫자 구성
#   banned_id : 불량 아이디 목록 (List)
#       size : 1 ~ len(user_id)
#       len  : 1 ~ 8
#       알파벳 소문자 & 숫자 & * 구성, 1개와만 매칭
# Output
#   제재 아이디 목록의 경우의

from itertools import combinations
def solution(user_id, banned_ids):
    answer = 0
    banned_id_regex = []
    for banned_id in banned_ids:
        banned_id_regex.append(banned_id.replace("*", '[a-z0-9]') + "$")

    userComb = combinations(user_id, len(banned_id_regex))
    for userId in userComb:
        if checkBanned(userId, banned_id_regex):
            answer += 1

    # user_id 중 banned_id로 만들어지는 모든 조합을 만들고
    # 확인..? -> 가능해..?
    return answer

from itertools import permutations
import re

def checkBanned(checkIds, bannedIds) -> bool:
    permuteCheckIds = permutations(checkIds, len(checkIds))
    returnVal = 0
    for permuteCheckId in permuteCheckIds:
        returnVal = 1
        for i in range(0, len(bannedIds)):
            if re.match(bannedIds[i], permuteCheckId[i]) is None:
                returnVal = 0
                break;
        if returnVal == 1:
            return True
    return False




print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
# print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
# print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))


# fradi frodo abc123 frodoc