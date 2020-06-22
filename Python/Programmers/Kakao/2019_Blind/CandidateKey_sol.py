# 1. Uniqueness : 유일하게 식별
# 2. Minimality : 꼭 필요한 속성들로만 구성

# Input : relation
# 2차원 문자열 배열
# 1 <= Column <= 8, 1 <= row <= 20
# 1 <= string <= 8
# Output : # of Candidate Key

def solution(relation):
    answer_list = list()
    for i in range(1, 1 << len(relation[0])):
        tmp_set = set()
        for j in range(len(relation)):
            tmp = ''
            for k in range(len(relation[0])):
                if i & (1 << k):
                    tmp += str(relation[j][k])
                tmp_set.add(tmp)
        if len(tmp_set) == len(relation):
            not_duplicate = True
            for num in answer_list:
                if (num & i) == num:
                    not_duplicate = False
                    break
            if not_duplicate:
                answer_list.append(i)

    return len(answer_list)

print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))
