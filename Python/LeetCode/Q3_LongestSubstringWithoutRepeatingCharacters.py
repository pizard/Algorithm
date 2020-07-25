class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        characterDict = {}
        answer = 0
        splitPos = 0
        for i, character in enumerate(s):
            if character in characterDict.keys():
                if splitPos < characterDict[character] + 1:
                    splitPos = characterDict[character] + 1
            if i + 1 - splitPos > answer:
                answer = i - splitPos + 1
            characterDict[character] = i
        return answer



sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb")) # 3
print(sol.lengthOfLongestSubstring("bbbbb")) # 1
print(sol.lengthOfLongestSubstring("pwwkew")) # 3
print(sol.lengthOfLongestSubstring("abba")) # 2
print(sol.lengthOfLongestSubstring(" ")) # 1
print(sol.lengthOfLongestSubstring("a")) # 1
print(sol.lengthOfLongestSubstring("au")) # 2