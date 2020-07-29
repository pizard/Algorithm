# Input
#   nums : array of n integers
# Output
#   합계가 0이 되는 유일한 조합
class Solution:
    def threeSum(self, nums):
        # 아니 이거 심하잖아.... 근데 왜 아래꺼가 더 빠른거야..?
        answer = set(); posNums = []; negNums = []; zeroNums = []
        for num in nums:
            if num > 0: posNums.append(num)
            elif num == 0 : zeroNums.append(num)
            else: negNums.append(num)
        posNums.sort()
        negNums.sort()
        posNums_c = set(posNums)
        negNums_c = set(negNums)

        # answer = set()
        # posNums = sorted([n for n in nums if n>0])
        # posNums_c = set(posNums)
        # zeroNums = [n for n in nums if n == 0]
        # negNums = sorted([n for n in nums if n<0])
        # negNums_c = set(negNums)



        for i in range(len(posNums)): # 1 Neg + 2 Pos
            for j in range(i+1, len(posNums)):
                if -(posNums[i] + posNums[j]) in negNums_c:
                    answer.add((-(posNums[i] + posNums[j]), posNums[i], posNums[j]))

        for i in range(len(negNums)): # 2 Neg + 1 Pos
            for j in range(i+1, len(negNums)):
                if -(negNums[i] + negNums[j]) in posNums_c:
                    answer.add((-(negNums[i] + negNums[j]), negNums[i], negNums[j]))

        if len(zeroNums) != 0: # 1 Pos & 0 & 1 Neg
            for posNum in posNums:
                if -posNum in negNums:
                    answer.add((-posNum, 0, posNum))

        if len(zeroNums) > 2:
            answer.add((0,0,0))

        return answer

sol = Solution()

sol.threeSum([-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0])

