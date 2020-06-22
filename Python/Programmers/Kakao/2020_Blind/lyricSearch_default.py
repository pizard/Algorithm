import re
def solution(words, queries):
    queriesAlignment = {}
    for query in queries:
        if not len(query) in queriesAlignment.keys():
            queriesAlignment[len(query)] = {}  # 길이 dict 생성
        if not "num" in queriesAlignment.keys():
            queriesAlignment[len(query)][query] = {"num" : 0, "regex" : keywordToregex(query)} # query dict 생성

    for word in words:
        if len(word) in queriesAlignment.keys():
            for queryAlignment in queriesAlignment[len(word)].values():
                if re.match(queryAlignment["regex"], word):
                    queryAlignment["num"] = queryAlignment["num"] + 1

    answer = []
    for query in queries:
        answer.append(queriesAlignment[len(query)][query]["num"])

    return answer


def keywordToregex(query):
    regex = query.replace(''.join(re.findall('\?', query)), "[A-Za-z]{" + str(len(re.findall('\?', query))) + "}")
    return regex




solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"])