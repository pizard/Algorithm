class Solution:
    def combinationSum(self, candidates, target):
        answer = []

        self.activator(answer, candidates, [], 0, target)
        print(answer)

        return 0

    def activator(self, answer, candidates, currComb, currSum, target):
        if currSum == target:
            answer.append(currComb)
        if currSum > target:
            return
        for i in range(0, len(candidates)):
            self.activator(answer, candidates[i:], currComb+[candidates[i]], currSum+candidates[i], target)

sol = Solution()

sol.combinationSum(candidates = [2,3,6,7], target = 7,)