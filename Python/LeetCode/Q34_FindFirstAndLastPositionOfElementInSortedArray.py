def binarySearch(answer, data, start, end, target, findMin=False, findMax=False):
   while start <= end:
        mid = (start + end) // 2
        if data[mid] == target:
            if findMin:
                if answer["min"] > mid: answer["min"] = mid
                binarySearch(answer, data, start, mid-1, target, True, False)
            if findMax:
                if answer["max"] < mid: answer["max"] = mid
                binarySearch(answer, data, mid+1, end, target, False, True)

            return
        elif data[mid] < target:
            start = mid+1
        else:
            end = mid-1
   return -1



class Solution:
    def searchRange(self, nums, target: int):
        answer = {"min": len(nums), "max":0}
        if binarySearch(answer, nums, 0, len(nums)-1, target, True, True) == -1:
            return [-1, -1]
        else:
            return[answer["min"], answer["max"]]



sol = Solution()

sol.searchRange(nums = [5,7,7,8,8,10], target = 8)
sol.searchRange(nums = [8,8,8,8,8,8,8], target = 8)
sol.searchRange(nums = [], target = 8)
