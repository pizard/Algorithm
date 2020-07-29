

# 5
# 4/1, 1/4
# 3/2, 2/3
# 3/1/1
# 2/2/1



# 4
# 3/1 -> 2/1/1, 1/2/1, 1/1/1/1
# 1/3 -> 1/2/1, 1/1/2, 1/1/1/1
# 2/2
# 1/3
# 2/1/1
# 1/1/1/1

# 3
# 2/1
# 1/2
# 1/1/1
# 2개 짜리...

# 2
# 1/1

# 1
# 1


# class Solution:
#     def generateParenthesis(self, n: int):
#         parenthesisTable = {i:set()for i in range(2,n+1)}
#         for i in range(2, n+1):
#             parenthesisTable[i].append(parenthesisTable)








def createParenthesis(answer, parenthesis, stack, n):
    if n == 0:
        if stack == 0:
            answer.add(parenthesis)
        else:
            pass
    elif stack == 0:
        createParenthesis(answer, parenthesis+"(", stack+1, n-1)
    elif stack > 0:
        createParenthesis(answer, parenthesis + "(", stack+1, n - 1)
        createParenthesis(answer, parenthesis + ")", stack-1, n - 1)


class Solution:
    def generateParenthesis(self, n: int):
        answer = set()
        createParenthesis(answer, "", 0,2*n)

        return answer
sol = Solution()
sol.generateParenthesis(3)
