class Solution:
    def maximalRectangle(self, matrix):
        # 1. matrix가 없는 경우 0 반환
        if not matrix or not matrix[0]:
            return 0
        ans = float('-inf')
        height = [0] * len(matrix[0])
        for row in matrix:
            for i in range(len(row)):
                height[i] = height[i]+1 if row[i] == '1' else 0
                ans = max(ans, height[i])
            cCount = 0
            prevVals = set() # 계산에 들어가는 이전까지의 값들
            for i, val in enumerate(height): #
                if val == 0:
                    cCount = 0
                else:
                    cCount += 1
                    if len(prevVals) == 0:
                        pass
                    else:
                        for prevVal in prevVals.copy():
                            if val > prevVal:
                                # 그대로, 추가
                                prevVals.add(val)
                            else:
                                prevVals.remove(prevVal)
                                cVal = cVal

                            ans = max(ans, cVal * cCount)
        return ans


sol = Solution()


# 6
sol.maximalRectangle([
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
])