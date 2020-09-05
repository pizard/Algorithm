class Solution:
    def trap(self, height):
        heightKinds = sorted(set(height), reverse=True)
        if len(heightKinds) == 0 or len(heightKinds) == 1:
            return 0


        heightKinds.remove(min(heightKinds))
        blockRow = []
        prevHeightKind = max(heightKinds)+1
        answer = 0

        for heightKind in heightKinds:
            if prevHeightKind - heightKind != 1:
                answer += (prevHeightKind - heightKind - 1) * (max(blockRow) - min(blockRow) - 1)
            blockRow = blockRow+[i for i, x in enumerate(height) if x == heightKind]
            answer += (prevHeightKind - heightKind) * (max(blockRow) - min(blockRow) - len(blockRow) + 1)
            prevHeightKind = heightKind
        answer += (prevHeightKind - 1) * (max(blockRow) - min(blockRow) - 1)

        return answer


sol = Solution()
# print(sol.trap([0,1,0,2,1,0,1,3,2,1,2,1])) # 6
# print(sol.trap([0,5,0,5,0])) # 5
# print(sol.trap([0,5,1,5,0])) # 4
# print(sol.trap([])) # 0
# print(sol.trap([1,1,1,1,1,1])) # 0

print(sol.trap([0,2,0])) # 0
print(sol.trap([0,2,4])) # 0

# 3 : 0
# 2 : 3 ~ 10, 3,7,8,10 -> 8칸 중 4칸 block : 4개
# ...
#