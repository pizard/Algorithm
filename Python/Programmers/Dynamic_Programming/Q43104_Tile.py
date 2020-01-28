def solution(N):
    answer, temp, answerBefore = 1, 1, 1

    for i in range(1, N):
        temp = answer
        answer = answerBefore + answer
        answerBefore = temp

    answer = answer * 2 + answerBefore * 2
    return answer