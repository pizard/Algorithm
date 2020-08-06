# O(log n)
# 방법 1 : 정렬 후 바이너리 서치 : log n * 2 = log n
# 방법 2 : 한번에 찾기
# ---------------------------------------------------------- #
# Solution 1

def binarySearch(data, target):
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (end + start) // 2
        if data[mid] == target:
            return mid
        elif data[mid] > target:
            end = mid-1
        elif data[mid] < target:
            start = mid+1
    return -1


class Solution:
    def search(self, nums, target: int) -> int:
        if len(nums) == 0:
            return -1
        minNum = min(nums)
        minNumIdx = nums.index(minNum)
        numsSort = nums[minNumIdx:] + nums[:minNumIdx]

        targetIdx = binarySearch(numsSort, target)
        if targetIdx == -1:
            return -1
        elif minNumIdx == 0:
            return targetIdx
        else:
            return (targetIdx-len(nums)+minNumIdx if target >= nums[0] else minNumIdx+targetIdx)

#


sol = Solution()
# print(sol.search([4,5,6,7,0,1,2], 3))
# print(sol.search(nums = [4,5,6,7,0,1,2], target = 0))
print(sol.search([1,3,5], 1)) # 0
print(sol.search([1,3,5], 3)) # 1
print(sol.search([1,3,5], 5)) # 2
# print(sol.search([4,5,6,7,0,1,2], 0))
# 1,2,3,4,5,6,7

print(sol.search([6,7,1,2,3,4,5], 6)) # 0
print(sol.search([6,7,1,2,3,4,5], 7)) # 1
print(sol.search([6,7,1,2,3,4,5], 1)) # 2
print(sol.search([6,7,1,2,3,4,5], 2))
print(sol.search([6,7,1,2,3,4,5], 3))
print(sol.search([6,7,1,2,3,4,5], 4))
print(sol.search([6,7,1,2,3,4,5], 5))

# 6,7,1,2,3,4,5
        # 시작 값과 비교
        # 1. 큰 경우
        #   왼쪽 이동!
        # 2. 작은 경우
        #   오른쪽 이동