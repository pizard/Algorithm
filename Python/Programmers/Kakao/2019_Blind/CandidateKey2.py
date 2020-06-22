# 1. Uniqueness : 유일하게 식별
# 2. Minimality : 꼭 필요한 속성들로만 구성

# Input : relation
# 2차원 문자열 배열
# 1 <= Column <= 8, 1 <= row <= 20
# 1 <= string <= 8
# Output : # of Candidate Key


from itertools import combinations
def checkCandidate(colLst, relation):
    tmp = [tuple([item[idx] for idx in colLst]) for item in relation]
    if len(set(tmp)) != len(relation):
        return False
    else:
        return True

def solution(relation):
    answer = 0
    rows = len(relation)
    cols = len(relation[0])
    colLst = range(cols)
    lst = []
    # 가능한 모든 조합 선택
    for leng in range(1, cols+1): # leng : 1 ~ # of column
        comb = combinations(colLst, leng)
        for n1 in list(comb): # 1개 조합, 2개 조합 ... n개 조합
            if checkCandidate(n1, relation):
                lst.append(set(n1))
    # 중복 제거
    for el1 in lst[:]:
        for el2 in lst[:]:
            if el1 == el1 & el2:
                if el1 != el2:
                    lst.remove(el2)
    return len(lst)


print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))
