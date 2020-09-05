class Solution:
    def largestRectangleArea(self, heights) -> int:
        l = 0
        r = len(heights)-1
        self.max = 0
        self.search(heights, l, r)

        return self.max

    def search(self, heights, l, r):
        while l<=r:
            if self.max < (r-l+1) * min(heights[l:r+1]):
                self.max = (r-l+1) * min(heights[l:r+1])
            if heights[l] < min(heights[l:r+1]):
                self.search(heights, l+1, r)
            elif heights[l] < min(heights[l:r+1]):
                self.search(heights, l, r-1)
            else:
                self.search(heights, l+1, r)
                self.search(heights, l, r-1)
                break;


sol = Solution()

print(sol.largestRectangleArea([2,1,5,6,2,2]))
print(sol.largestRectangleArea([1]))
print(sol.largestRectangleArea([6,4,2,0,3,2,0,3,1,4,5,3,2,7,5,3,0,1,2,1,3,4,6,8,1,3]))

print(sol.largestRectangleArea([5,5,1,7,1,1,5,2,7,6]))




