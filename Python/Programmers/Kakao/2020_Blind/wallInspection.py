import sys
import os



def permutation(candidates, Prepermuation, res):
    if len(candidates) == 0: res.append(Prepermuation); return
    else:
        for i in range(len(candidates)):
            permutation(candidates[:i]+candidates[i+1:], Prepermuation + [ candidates[i] ], res)
        return


def solution(n, weak, dist):
    # complete search
    dist.sort(reverse = True)

    for i in range(1, len(dist)+1):
        permutations = [];
        permutation(dist[:i], [], permutations)
        print(permutations)

def solution2(n, weak, dist):
    dist.sort()
    weak_dist = []

    max_dist = 0
    for i in range(len(weak)):
        if len(weak) > 1:
            # num of weak 2개 이상
            if i == 0:
                weak_dist.append(n-weak[len(weak)-1]+weak[0])
            else:
                weak_dist.append(weak[i]-weak[i-1])
            if max_dist < weak_dist[i]:
                max_dist = weak_dist[i]
        else:
            # num of weak 1개
            return 1

    print(weak_dist)
    print(max_dist)

    return -1

n = 2
print("2") if n > 1 else \
    print("1")


print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
print('-------------------------------------')
print(solution(12, [1, 3, 4, 9, 10],[3, 5, 7]))

