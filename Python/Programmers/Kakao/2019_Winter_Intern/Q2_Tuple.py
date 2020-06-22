# tuple : 셀 수 있는 수량의 순서있는 열거 또는 어떤 순서를 따르는 요소들의 모음
#   1. 중복 가능
#   2. 순서 존재

# Input
#   s :
#       length : 5 ~ 1,000,000
#       구조 : '#'. '{', '}', ','
#

# Output
#   s가 표현하는 튜플



from collections import Counter
def solution(s):
    answer = []
    for val in Counter(s.replace("{","").replace("}","").split(",")).most_common():
        answer.append(int(val[0]))
    return answer



# solution("{{2},{2,1},{2,1,3},{2,1,3,4}}")
solution("{{4,2,3},{3},{2,3,4,1},{2,3}}") # [3, 2, 4, 1]