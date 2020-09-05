class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cTable = {} # character Table
        tTable = {} # target Table
        for cT in t:
            if cT in cTable.keys():
                tTable[cT] += 1
            else:
                tTable[cT] = 1

        lenT = len(t)
        answerLen = float("inf")
        answer = ""
        for i, c in enumerate(s):
            if c in t:
                if c not in cTable.keys():
                    cTable[c] = i
                else:
                    cTable[c] = [i]
                if len(cTable) == lenT:
                    lenA = max(cTable.values()) - min(cTable.values())
                    if answerLen > lenA:
                        answer = s[min(cTable.values()):max(cTable.values())+1]
                        answerLen = lenA
        return answer


sol = Solution()
print(sol.minWindow("aa","aa"))
print(sol.minWindow("ADOBECODEBANC","ABC"))