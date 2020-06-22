from itertools import cycle

def solution(food_times, k):
    answer = 0
    sortedFoodTimes = sorted(food_times)

    k += 1
    prevValue = 0
    while True:
        value = sortedFoodTimes[0]
        valueGap = value - prevValue
        prevValue = value

        # Step 1
        if k > valueGap * len(sortedFoodTimes):
            k -= valueGap * len(sortedFoodTimes)
            while sortedFoodTimes[0] <= value:
                sortedFoodTimes.pop(0)
                if len(sortedFoodTimes) == 0:
                    return -1
        # Step 2
        else:
            k = k % len(sortedFoodTimes) if k % len(sortedFoodTimes) != 0 else len(sortedFoodTimes)

            while k != 0:
                for i, time in enumerate(food_times):
                    if sortedFoodTimes[0] > time:
                        # 해당 값보다 작은 경우 -> 넘어가기
                        pass

                    elif sortedFoodTimes[0] <= time:
                        # 해당 값보다 큰 경우 ->
                        k -= 1
                        answer = i+1
                    if k == 0:
                        break;
            break

    return answer


print(solution([3, 1, 2], 5)) # 1
print(solution([3, 2, 1], 5)) # 1
print(solution([4,1,1,5], 4)) # 1
print(solution([4,1,1,5], 3)) # 4
print(solution([4,1,1,5], 0)) # 1
print(solution([4,1,1,5], 11)) # -1

print(solution([4, 3, 5, 6, 2], 7)) # 3
print(solution([4, 3, 5, 6, 2], 0)) # 1
print(solution([3,1,1,1,2,4,3],12)) # 6