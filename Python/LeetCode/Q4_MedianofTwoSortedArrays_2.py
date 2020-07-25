# There are two sorted arrays nums1 and nums2 of size m and n respectively.
#
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
#
# You may assume nums1 and nums2 cannot be both empty.

class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        sortedList = []
        while True:
            if len(nums1) == 0:
                sortedList.append(nums2)
                break;
            elif len(nums2) == 0:
                sortedList.append(nums1)
                break;

            if nums1[0] < nums2[0]:
                sortedList.append(nums1.pop(0))
            else:
                sortedList.append(nums2.pop(0))

        result = -1
        length = len(sortedList)
        if length % 2 == 0:
            # even Num
            result = (sortedList[length//2-1] + sortedList[length//2]) / 2
        else:
            # odd Num
            result = sortedList[length // 2]
        return result

# 0, 1, 2, 3, 4, 5, 6, 7 -> 8개
# 0, 1, 2, 3, 4, 5, 6 -> 7개

solution = Solution()
print(solution.findMedianSortedArrays([1,3,10,8,7],[2,5,9,6]))
print(solution.findMedianSortedArrays([1,2],[3,4]))
