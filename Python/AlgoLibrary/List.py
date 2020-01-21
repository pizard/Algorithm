# answers = makeAnswerList(3, False, [0])
import itertools




def createList(length, replication, notContainNums):
    answer = []
    startNum, endNum= 10**(length-1), 10**length

    for x in range(startNum, endNum):
        checkTemp = set(str(x))
        if replication == False:
            if len(checkTemp) != length:
                continue
        for notContainNum in notContainNums:
            if str(notContainNum) not in checkTemp:
                answer.append(x)
    return answer

# answers = list(itertools.permutations([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)) # 3개로 순열 생성