from itertools import product
class Solution:
    def letterCombinations(self, digits: str):
        dialDict = {2: ["a","b","c"], 3:["d","e","f"],
                    4: ["g", "h", "i"], 5: ["j", "k", "l"], 6: ["m", "n", "o"],
                    7: ["p", "q", "r", "s"], 8: ["t", "u", "v"], 9: ["w", "x", "y", "z"]}
        dialTable = []
        for digit in digits:
            dialTable.append(dialDict[int(digit)])

        return "" if dialTable == [] else ["".join(t) for t in list(product(*dialTable))]

sol = Solution()

# print(sol.letterCombinations("23"))
print(sol.letterCombinations(""))