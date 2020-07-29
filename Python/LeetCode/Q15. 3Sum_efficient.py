# Input
#   nums : array of n integers
# Output
#   합계가 0이 되는 유일한 조합
import itertools
class Solution:
    def threeSum(self, nums):
        answer = []
        posNums = []
        negNums = []
        zeroNums = []
        for num in nums:
            if num > 0: posNums.append(num)
            elif num == 0 : zeroNums.append(num)
            else: negNums.append(num)

        posComb2 = itertools.combinations(posNums, 2) # 2 Pos & 1 Neg
        for candidate in posComb2:
            if -sum(candidate) in negNums:
                answer.append([-sum(candidate)] + list(candidate))

        negComb2 = itertools.combinations(negNums, 2) # 1 Pos & 2 Neg
        for candidate in negComb2:
            if -sum(candidate) in posNums:
                answer.append(list(candidate) + [-sum(candidate)])

        if len(zeroNums) != 0: # 1 Pos & 0 & 1 Neg
            for posNum in posNums:
                if -posNum in negNums:
                    answer.append([-posNum, 0, posNum])
        if len(zeroNums) >= 3:
            answer.append([0,0,0])

        return list(set([tuple(sorted(answer)) for answer in answer]))

sol = Solution()
# print(sol.threeSum([0,0,0]))
# print(sol.threeSum([-1, 0, 1, 2, -1, -4]))
# sol.threeSum([-2,0,0,2,2])
# sol.threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6])

sol.threeSum([-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0])

