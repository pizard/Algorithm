# There are two sorted arrays nums1 and nums2 of size m and n respectively.
#
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
#
# You may assume nums1 and nums2 cannot be both empty.

import math

def binary_search_insert(target, data, direction):
    # direction : True (index : →) / False (index : ← )
    start = 0
    end = len(data) - 1
    if len(data) == 0:
        return 0
    while start <= end:
        mid = (start + end) // 2

        if data[mid] == target:
            return mid
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    if direction:
        if target > data[mid]:
            mid += 1

    else:
        if target > data[mid]:
            mid -= 1
    return mid


class SortedList:
    def __init__(self):
        self.numList = []
    def insertList(self, insertList):
        for insertValue in insertList:
            self.numList.insert(binary_search_insert(insertValue, self.numList, True), insertValue)



class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        sortedList = SortedList()
        sortedList.insertList(nums1)
        sortedList.insertList(nums2)


        result = -1
        length = len(sortedList.numList)
        if length % 2 == 0:
            # even Num
            result = (sortedList.numList[math.floor(length/2-1)] + sortedList.numList[math.floor(length/2)]) / 2
        else:
            # odd Num
            result = sortedList.numList[math.floor(length / 2)]
        return result

# 0, 1, 2, 3, 4, 5, 6, 7 -> 8개
# 0, 1, 2, 3, 4, 5, 6 -> 7개

solution = Solution()
print(solution.findMedianSortedArrays([1,3,10,8,7],[2,5,9,6]))
print(solution.findMedianSortedArrays([1,2],[3,4]))
