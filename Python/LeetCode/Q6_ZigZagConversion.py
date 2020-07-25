class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        zigzagTable = ["" for i in range(numRows)]

        for i, character in enumerate(s):
            pos1 = i % (2 * (numRows -1))
            if pos1 < numRows:
                zigzagTable[pos1] += character
            else:
                zigzagTable[2 * numRows-pos1-2] += character

        answer = ''.join(zigzagTable)

        return answer

sol = Solution()
sol.convert("PAYPALISHIRING", 3)
sol.convert("PAYPALISHIRING", 4)
'''
1        9
2     8 10
3   7
4 6
5

n+1
n+

'''