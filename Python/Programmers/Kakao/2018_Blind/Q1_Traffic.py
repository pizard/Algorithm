# Input
#   lines (Array, length : 1 ~ 2000)
#       S(응답완료시간) : '2016-09-15 hh:mm:ss.sss' (오름차순)
#       T(처리시간) : 최대 소수점 셋째자리 & s
#           0.001 ~ 3.000
# Output
#   초당 최대 처리량 : 임의시간에서 1초간 처리하는 요청의 최대 갯수

from datetime import datetime
def solution(lines):
    answer = 0
    processNum = 0
    processInfo = []

    for line in reversed(lines):
        end = datetime.strptime(" ".join(line.split(" ")[:2]), "%Y-%m-%d %H:%M:%S.%f").timestamp()


# print(solution(["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s",
#  "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s",
#  "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s",
#  "2016-09-15 21:00:02.066 2.62s"]))
#




