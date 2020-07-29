# Input
#   nums : array of n integers
# Output
#   합계가 0이 되는 유일한 조합
import itertools
class Solution:
    def threeSum(self, nums):
        answer = []
        comb = list(itertools.combinations(nums, 3)) # 3개 짜리 조합 생성
        for candidate in comb:
            if sum(candidate) == 0: # 합산이 0인 경우 추가
                if sorted(list(candidate)) not in answer:
                    answer.append(sorted(list(candidate)))
        return answer


sol = Solution()
sol.threeSum([-1, 0, 1, 2, -1, -4])