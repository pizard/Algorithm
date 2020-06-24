from itertools import product
import re

def check(user_id, banned_id):
    return True if re.match(banned_id.replace("*","."), user_id) is not None else False

def solution(user_ids, banned_ids):
    answer = set()
    # 1. 각 banned_id에 적용되는 user_id 검사
    bannedCandidate = [[] for col in range(0, len(banned_ids))]
    for i, banned_id  in enumerate(banned_ids):
        for user_id in user_ids:
            if check(user_id, banned_id):
                bannedCandidate[i].append(user_id)

    # 2. 모든 조합 생성
    bannedCandidateComb = product(*bannedCandidate)

    # 3. 중복 제거
    bannedId_len = len(banned_ids)
    for bannedCandidateVal in bannedCandidateComb:
        if len(set(bannedCandidateVal)) == bannedId_len:
            answer.add(tuple(sorted(bannedCandidateVal)))

    return len(answer)


print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))
