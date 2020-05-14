# 1 depth : 단어 길이
# 2 depth : 첫 문자
# 3 depth : 둘째 문자
# ...

# 1 depth : 단어 길이
class Trie:
    def __init__(self):
        self.wordLength = {} # 단어의 길이 (length : Node)
        self.wordCount = 0

    def insertWord(self, word): # 단어 길이에 기반한 Node 추가
        if len(word) not in self.wordLength.keys(): # 해당 길이 Node 생성
            self.wordLength[len(word)] = Node()

        self.wordLength[len(word)].insertNode(word)  # length -> char : word 추가
        self.wordCount += 1


    def getQueryNum(self, query):
        if query == "?" * len(query):                         # query가 전부 ?인 경우
            return self.wordLength[len(query)].childCount
        elif len(query) not in self.wordLength.keys():        # 해당 길이가 없는 경우
            return 0
        elif query[:1] not in self.wordLength[len(query)].child.keys(): # 해당 단어의 첫 문자로 시작하는 단어가 없는 경우
            return 0
        else:
            return self.wordLength[len(query)].child[query[:1]].getQueryNum(query)

# 2 depth : 첫 문자
class Node:
    def __init__(self, char = None):
        self.char = char      # 해당 Node의 문자
        self.childCount = 0 # 하위 단어의 갯수
        self.child = {}     # 하위 단어


    def insertNode(self, word): # 첫번째 문자에 기반한 Node 추가
        self.childCount += 1
        if word[:1] not in self.child.keys():
            self.child[word[:1]] = Node(word[:1])

        if len(word) > 1:
            self.child[word[:1]].insertNode(word[1:])


    def getQueryNum(self, query):
        queryNum = self.childCount
        node = self

        for char in query[1:]:
            if char == "?":
                return queryNum
            elif char not in node.child.keys():
                return 0
            else:
                node = node.child[char]
                queryNum = node.childCount
        return queryNum


def solution(words, queries):
    front = Trie()
    back = Trie()
    for word in words:
        front.insertWord(word)
        back.insertWord(word[::-1])
    answer = []

    for query in queries:
        if query[:1] == "?":
            query = query[::-1]
            answer.append(back.getQueryNum(query))
        else:
            answer.append(front.getQueryNum(query))
    print(answer)
    return answer
solution(["frodo", "front", "frost", "frozen", "frame", "kakao", ""], ["", "?????", "fro??", "????o", "fr???", "fro???", "pro?"])
solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["?????", "fro??", "????o", "fr???", "fro???", "pro?"])
solution(["frodo", "front", "frost", "frosa", "frodt", "frwme", "frozen", "frame", "kakao", ""], ["", "?????", "fro??", "????o", "fr???", "fro???", "pro?"])
solution(["frodo", "front", "frost", "frosa", "frodt", "frwme", "frozen", "frame", "kakao"], ["?????", "fro??", "????o", "fr???", "fro???", "pro?"])




